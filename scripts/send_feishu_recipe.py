#!/usr/bin/env python3
"""Send a recipe monitor Markdown note to a Feishu custom bot webhook."""

from __future__ import annotations

import argparse
import base64
import hashlib
import hmac
import json
import os
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path


MAX_TEXT_LENGTH = 3800


def build_text(markdown: str, source_path: Path) -> str:
    keyword = os.environ.get("FEISHU_KEYWORD", "recipe").strip() or "recipe"
    text = markdown.strip()
    if len(text) > MAX_TEXT_LENGTH:
        text = text[: MAX_TEXT_LENGTH - 80].rstrip() + "\n\n...（内容较长，已截断；完整版本见 Obsidian）"
    return f"{keyword}\n今日儿童友好菜谱已更新\n来源：{source_path.name}\n\n{text}"


def build_payload(text: str, secret: str | None) -> dict:
    payload: dict = {
        "msg_type": "text",
        "content": {
            "text": text,
        },
    }

    if secret:
        timestamp = str(int(time.time()))
        string_to_sign = f"{timestamp}\n{secret}"
        digest = hmac.new(
            string_to_sign.encode("utf-8"),
            b"",
            digestmod=hashlib.sha256,
        ).digest()
        payload["timestamp"] = timestamp
        payload["sign"] = base64.b64encode(digest).decode("utf-8")

    return payload


def post_json(webhook_url: str, payload: dict) -> tuple[int, str]:
    data = json.dumps(payload, ensure_ascii=False).encode("utf-8")
    request = urllib.request.Request(
        webhook_url,
        data=data,
        headers={"Content-Type": "application/json; charset=utf-8"},
        method="POST",
    )

    with urllib.request.urlopen(request, timeout=20) as response:
        body = response.read().decode("utf-8", errors="replace")
        return response.status, body


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("markdown_file", type=Path, help="Recipe monitor markdown file to send")
    parser.add_argument("--dry-run", action="store_true", help="Print payload instead of sending")
    args = parser.parse_args()

    if not args.markdown_file.exists():
        print(f"Markdown file not found: {args.markdown_file}", file=sys.stderr)
        return 2

    webhook_url = os.environ.get("FEISHU_WEBHOOK_URL") or os.environ.get("FEISHU_BOT_WEBHOOK")
    secret = os.environ.get("FEISHU_WEBHOOK_SECRET")

    markdown = args.markdown_file.read_text(encoding="utf-8")
    payload = build_payload(build_text(markdown, args.markdown_file), secret)

    if args.dry_run:
        print(json.dumps(payload, ensure_ascii=False, indent=2))
        return 0

    if not webhook_url:
        print(
            "Missing FEISHU_WEBHOOK_URL or FEISHU_BOT_WEBHOOK environment variable.",
            file=sys.stderr,
        )
        return 2

    try:
        status, body = post_json(webhook_url, payload)
    except urllib.error.URLError as exc:
        print(f"Failed to send Feishu webhook: {exc}", file=sys.stderr)
        return 1

    print(f"Feishu webhook status: {status}")
    print(body)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
