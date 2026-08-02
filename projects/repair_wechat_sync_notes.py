from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

import ftfy


FRONTMATTER_RE = re.compile(r"\A(?:\ufeff)?---\n.*?\n---\n?", re.S)
ID_LINE_RE = re.compile(r"(?m)^id:\s*([0-9a-fA-F-]+)\s*$")
FEEDBACK_RE = re.compile(r"(?m)^内容效果不满意？\[点此反馈\]\([^)]+\)\s*$")
IMAGE_RE = re.compile(r"^!\[\[[^\]]+\]\]$")
IMAGE_ALIAS_RE = re.compile(r"!\[\[(attachments/笔记同步图片/[^\]|]+)(?:\|[^\]]*)?\]\]")


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def write_text(path: Path, text: str) -> None:
    path.write_text(text, encoding="utf-8", newline="\n")


def chinese_score(text: str) -> int:
    cjk = len(re.findall(r"[\u4e00-\u9fff]", text))
    bad = text.count("\ufffd") * 8
    bad += len(re.findall(r"[鍏寰绗旇鍚屾]", text)) * 2
    bad += text.count("�?") * 8
    return cjk - bad


def clean_feedback(text: str) -> str:
    return FEEDBACK_RE.sub("", text)


def dedupe_image_runs(text: str) -> str:
    lines = text.splitlines()
    result: list[str] = []
    i = 0
    while i < len(lines):
        if IMAGE_RE.match(lines[i].strip()):
            start = i
            while i < len(lines) and (IMAGE_RE.match(lines[i].strip()) or not lines[i].strip()):
                i += 1
            block = lines[start:i]
            compact = [line for line in block if line.strip()]
            if compact and len(compact) % 2 == 0:
                half = len(compact) // 2
                if compact[:half] == compact[half:]:
                    compact = compact[:half]
            if compact:
                result.extend(compact)
                result.append("")
            continue
        result.append(lines[i])
        i += 1
    while result and result[-1] == "":
        result.pop()
    return "\n".join(result)


def rebuild_from_last_copy(text: str) -> tuple[str, bool]:
    id_matches = list(ID_LINE_RE.finditer(text))
    if len(id_matches) <= 1:
        return text, False
    fm = FRONTMATTER_RE.match(text)
    if not fm:
        return text, False
    last = id_matches[-1]
    delimiter = text.find("\n---", last.end())
    if delimiter == -1:
        return text, False
    delimiter_end = text.find("\n", delimiter + 1)
    if delimiter_end == -1:
        return text, False
    candidate = text[delimiter_end + 1 :].lstrip("\n")
    candidate = clean_feedback(candidate)
    candidate = dedupe_image_runs(candidate).strip()
    if chinese_score(candidate) < 20:
        return text, False
    rebuilt = fm.group(0).rstrip() + "\n\n" + candidate + "\n"
    return rebuilt, True


def normalize_meta_punctuation(text: str) -> str:
    return re.sub(
        r"(?m)^(公众号名称|作者名称|发布时间)\s*:\s*",
        lambda m: f"{m.group(1)}：",
        text,
    )


def cleanup_artifacts(text: str) -> str:
    text = IMAGE_ALIAS_RE.sub(r"![[\1]]", text)
    text = re.sub(r"(?m)^libpng warning:.*$", "", text)
    text = text.replace("![]]", "")
    text = re.sub(r"(?m)^author:\s*([^\n]+?)source:\s*", r"author: \1\nsource: ", text)
    text = text.replace("source: 微信公众�?url:", "source: 微信公众号\nurl:")
    text = text.replace("source: 微信公众�\nurl:", "source: 微信公众号\nurl:")
    text = re.sub(r"(?m)^发布时间(20\d{2}-\d{2}-\d{2}\s+\d{2}:\d{2})$", r"发布时间：\1", text)
    text = text.replace("�?026", "2026")
    text = text.replace("�?025", "2025")
    text = text.replace("�?024", "2024")
    text = text.replace("�?023", "2023")
    text = text.replace("锟?", "")
    text = text.replace("锟�", "")
    text = text.replace("�?*", "。*")
    text = text.replace("�?", "")
    text = text.replace("�", "")
    return text


def cleanup_spacing(text: str) -> str:
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip() + "\n"


def repair_text(text: str) -> tuple[str, dict[str, bool]]:
    changed = {"rebuilt": False, "ftfy": False, "feedback": False}
    working = text.replace("\ufeff", "", 1).replace("\r\n", "\n").replace("\r", "\n")

    rebuilt, did_rebuild = rebuild_from_last_copy(working)
    if did_rebuild:
        working = rebuilt
        changed["rebuilt"] = True

    cleaned = clean_feedback(working)
    if cleaned != working:
        working = cleaned
        changed["feedback"] = True

    fixed = ftfy.fix_text(working)
    fixed = normalize_meta_punctuation(fixed)
    fixed = cleanup_artifacts(fixed)
    fixed = cleanup_spacing(fixed)
    if fixed != working:
        working = fixed
        changed["ftfy"] = True

    return working, changed


def should_scan(path: Path, text: str) -> bool:
    if path.parts and any(part in {".obsidian", "attachments"} for part in path.parts):
        return False
    hints = (
        "mp.weixin.qq.com" in text
        or "笔记同步助手" in text
        or "绗旇鍚屾" in text
        or "公众号名称" in text
        or "鍏紬鍙峰悕绉" in text
        or "\ufffd" in text
    )
    return hints


def iter_markdown_files(root: Path) -> list[Path]:
    return sorted(p for p in root.rglob("*.md") if ".obsidian" not in p.parts and "attachments" not in p.parts)


def main() -> None:
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="backslashreplace")
    except Exception:
        pass
    parser = argparse.ArgumentParser()
    parser.add_argument("--path", help="Only repair one file")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    root = Path(".")
    if args.path:
        targets = [Path(args.path)]
    else:
        targets = iter_markdown_files(root)

    changed_files: list[tuple[Path, dict[str, bool]]] = []
    scanned = 0

    for path in targets:
        if not path.exists():
            continue
        text = read_text(path)
        if not should_scan(path, text):
            continue
        scanned += 1
        repaired, flags = repair_text(text)
        if repaired != text:
            changed_files.append((path, flags))
            if not args.dry_run:
                write_text(path, repaired)

    print(f"scanned={scanned}")
    print(f"changed={len(changed_files)}")
    print(f"rebuilt={sum(1 for _, f in changed_files if f['rebuilt'])}")
    print(f"ftfy={sum(1 for _, f in changed_files if f['ftfy'])}")
    print(f"feedback_removed={sum(1 for _, f in changed_files if f['feedback'])}")
    for path, flags in changed_files[:50]:
        kinds = ",".join(k for k, v in flags.items() if v)
        print(f"{path}\t{kinds}")


if __name__ == "__main__":
    main()
