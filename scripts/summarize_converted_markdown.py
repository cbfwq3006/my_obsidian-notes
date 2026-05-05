from __future__ import annotations

import csv
from collections import defaultdict
from pathlib import Path


ROOT = Path(r"E:\sl_obsidian\converted_markdown\组织生活会")


def read_csv(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        return []
    with path.open("r", encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def group_name_from_source(source: str) -> str:
    try:
        rel = Path(source).relative_to(r"D:\work\2026\4\5 组织生活会")
        return rel.parts[0] if rel.parts else "(root)"
    except Exception:
        parts = Path(source).parts
        return parts[-2] if len(parts) > 1 else "(unknown)"


def main() -> int:
    converted = read_csv(ROOT / "converted.csv")
    failed = read_csv(ROOT / "failed.csv")
    unsupported = read_csv(ROOT / "unsupported.csv")

    groups: dict[str, dict[str, list[dict[str, str]]]] = defaultdict(lambda: defaultdict(list))
    for row in converted:
        groups[group_name_from_source(row["source"])]["converted"].append(row)
    for row in failed:
        groups[group_name_from_source(row["source"])]["failed"].append(row)
    for row in unsupported:
        groups[group_name_from_source(row["source"])]["unsupported"].append(row)

    lines = [
        "# 组织生活会材料转换汇总",
        "",
        f"转换目录：`{ROOT}`",
        "",
        "## 总览",
        "",
        f"- 已转换：{len(converted)}",
        f"- 转换失败：{len(failed)}",
        f"- 暂不支持：{len(unsupported)}",
        "",
        "## 后续逻辑审核建议",
        "",
        "- 先按每个支部检查材料是否齐全：会议纪要、支部班子对照检查、个人发言材料、整改清单、民主评议结果报告。",
        "- 再检查会议程序是否完整：准备情况、班子对照、个人发言、批评与自我批评、民主测评、结果研究、整改清单。",
        "- 然后检查数据一致性：应到/实到人数、参评人数、优秀比例、整改问题是否与征求意见和查摆问题对应。",
        "- 最后检查文本逻辑：问题是否具体、原因是否对应、整改措施是否可执行、时限和责任是否明确。",
        "",
        "## 分支部转换情况",
        "",
        "| 支部/单位 | 已转换 | 失败 | 暂不支持 |",
        "| --- | ---: | ---: | ---: |",
    ]

    for group in sorted(groups):
        bucket = groups[group]
        lines.append(
            f"| {group} | {len(bucket['converted'])} | {len(bucket['failed'])} | {len(bucket['unsupported'])} |"
        )

    if failed:
        lines.extend(["", "## 转换失败文件", ""])
        for row in failed:
            lines.append(f"- `{row['source']}`：{row.get('error', '')}")

    if unsupported:
        by_ext: dict[str, int] = defaultdict(int)
        for row in unsupported:
            by_ext[row["extension"]] += 1
        lines.extend(["", "## 暂不支持文件类型", ""])
        for ext, count in sorted(by_ext.items(), key=lambda item: (-item[1], item[0])):
            lines.append(f"- `{ext}`：{count} 个")

    (ROOT / "conversion-summary.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(ROOT / "conversion-summary.md")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
