from __future__ import annotations

import csv
import re
from dataclasses import dataclass, field
from pathlib import Path


ROOT = Path(r"E:\sl_obsidian\converted_markdown\组织生活会")
OUT_MD = ROOT / "个人对照检查材料审核报告.md"
OUT_CSV = ROOT / "personal-check-audit.csv"


ASPECTS = {
    "创新理论": ["创新理论", "理论学习", "学习贯彻"],
    "党性修养": ["党性", "政治纪律", "组织纪律", "纪律", "规矩"],
    "联系服务群众": ["联系服务群众", "服务群众", "群众"],
    "先锋模范": ["先锋模范", "模范作用", "示范带头"],
    "作风建设": ["作风", "树新风", "形式主义", "担当作为"],
    "廉洁自律": ["廉洁", "纪律作风", "廉政", "从严治党", "底线"],
}

PROBLEM_MARKERS = ["不足", "不够", "欠缺", "存在", "未能", "缺乏", "不到位", "差距", "薄弱", "不强", "不足以"]
CONCRETE_MARKERS = ["例如", "比如", "具体", "实际", "项目", "客户", "群众", "支部", "网格", "岗位", "工作中", "学习", "次数", "小时", "篇", "次", "月", "年"]
BAD_THIRD_PERSON = ["班子成员", "部分党员干部", "部分同志", "有的党员", "个别党员", "一些党员"]
BAD_CONTRAST_PATTERNS = ["虽然", "但是", "尽管", "却"]


@dataclass
class AuditResult:
    group: str
    name: str
    file: str
    source: str
    char_count: int
    line_count: int
    missing_aspects: list[str] = field(default_factory=list)
    weak_aspects: list[str] = field(default_factory=list)
    no_previous整改: bool = False
    no_rectification: bool = False
    third_person_hits: list[str] = field(default_factory=list)
    contrast_hits: list[str] = field(default_factory=list)
    too_short: bool = False
    problem_section_ratio_low: bool = False
    issues: list[str] = field(default_factory=list)

    @property
    def level(self) -> str:
        if self.missing_aspects or self.no_previous整改 or self.too_short:
            return "不达标"
        if self.weak_aspects or self.third_person_hits or self.contrast_hits or self.problem_section_ratio_low or self.no_rectification:
            return "需修改"
        return "基本达标"


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore")


def source_from_text(text: str) -> str:
    match = re.search(r"^Source: `(.+?)`", text, re.M)
    return match.group(1) if match else ""


def group_from_path(path: Path) -> str:
    rel = path.relative_to(ROOT)
    return rel.parts[0] if len(rel.parts) > 1 else "(root)"


def is_personal_material(path: Path, text: str) -> bool:
    name = path.name
    non_personal = [
        "会议纪要", "整改清单", "问题清单", "查摆问题清单", "规范化要求", "工作汇报",
        "整改落实情况", "民主评议", "结果报告", "支部委员会", "支部对照", "支部班子",
        "班子发言", "支委班子", "党支部发言", "党支部材料", "支部材料",
    ]
    if any(k in name for k in non_personal):
        return False
    if "支部委员会" in name or "支部对照" in name or "班子" in name or "党支部发言" in name:
        return False
    if "参考模板" in name or "模板" in name:
        return False
    if any(k in name for k in ["个人", "发言", "对照检查", "发言提纲"]):
        return True
    if "我" in text and "查摆" in text and "整改" in text:
        return True
    return False


def infer_name(path: Path) -> str:
    stem = path.stem
    patterns = [
        r"个人发言材料[-_.：—]*([^（）()0-9vV]+)",
        r"个人对照检查材料[-_.：—]*([^（）()0-9vV]+)",
        r"发言提纲[-_.：—]*([^（）()0-9vV]+)",
        r"发言材料[-_.：—]*([^（）()0-9vV]+)",
        r"[-_—]([一-龥]{2,4})(?:\s|\(|（|$)",
        r"^([一-龥]{2,4})[+_.-]",
    ]
    for pattern in patterns:
        match = re.search(pattern, stem)
        if match:
            value = re.sub(r"(办公室|客服部|支部书记|宣传委员|组织委员|纪检委员|青年委员|党支部|人力资源部党支部|市场部|综服中心|数字化与稽核中心)", "", match.group(1))
            value = value.strip(" -_—.（）()")
            if 2 <= len(value) <= 4:
                return value
    return stem


def section_after_problem_heading(text: str) -> str:
    matches = list(re.finditer(r"(查摆|存在的?问题|问题查摆|突出问题)", text))
    if not matches:
        return ""
    start = matches[0].start()
    later = re.search(r"\n[一二三四五六七八九十]+[、.．]\s*(原因|根源|整改|努力方向|剖析)", text[start:])
    if later:
        return text[start:start + later.start()]
    return text[start:]


def aspect_snippet(text: str, keywords: list[str]) -> str:
    positions = [text.find(k) for k in keywords if text.find(k) >= 0]
    if not positions:
        return ""
    start = max(0, min(positions) - 80)
    end = min(len(text), min(positions) + 700)
    return text[start:end]


def audit_file(path: Path) -> AuditResult:
    text = read_text(path)
    plain = re.sub(r"\s+", "", text)
    group = group_from_path(path)
    result = AuditResult(
        group=group,
        name=infer_name(path),
        file=str(path),
        source=source_from_text(text),
        char_count=len(plain),
        line_count=text.count("\n") + 1,
    )

    problem_text = section_after_problem_heading(text) or text
    problem_plain = re.sub(r"\s+", "", problem_text)

    for aspect, keywords in ASPECTS.items():
        snippet = aspect_snippet(problem_text, keywords)
        if not snippet:
            result.missing_aspects.append(aspect)
            continue
        if not any(marker in snippet for marker in PROBLEM_MARKERS):
            result.weak_aspects.append(f"{aspect}：未见明显问题表述")
            continue
        if not any(marker in snippet for marker in CONCRETE_MARKERS):
            result.weak_aspects.append(f"{aspect}：问题偏空，缺少具体事例/岗位结合")

    if not re.search(r"(上年度|2024年度|上一年度).{0,80}(整改|落实|销号|完成)", text, re.S):
        result.no_previous整改 = True

    if not re.search(r"(整改措施|努力方向|下一步|改进措施|整改方向)", text):
        result.no_rectification = True

    result.third_person_hits = [hit for hit in BAD_THIRD_PERSON if hit in text]
    result.contrast_hits = [hit for hit in BAD_CONTRAST_PATTERNS if hit in text]
    result.too_short = result.char_count < 3000

    if len(problem_plain) < max(800, result.char_count * 0.28):
        result.problem_section_ratio_low = True

    if result.missing_aspects:
        result.issues.append("六个方面查摆不完整：" + "、".join(result.missing_aspects))
    if result.weak_aspects:
        result.issues.append("部分方面问题表述偏弱：" + "；".join(result.weak_aspects[:3]))
    if result.no_previous整改:
        result.issues.append("未见上年度组织生活会问题逐项整改落实情况")
    if result.no_rectification:
        result.issues.append("未见明确整改措施/努力方向")
    if result.third_person_hits:
        result.issues.append("出现不应使用的第三人称表述：" + "、".join(result.third_person_hits))
    if result.contrast_hits:
        result.issues.append("出现先扬后抑/转折风险词：" + "、".join(result.contrast_hits))
    if result.too_short:
        result.issues.append("篇幅明显偏短，可能不足2页")
    if result.problem_section_ratio_low:
        result.issues.append("问题查摆和原因剖析占比偏低，可能不足全文1/2")

    return result


def write_csv(results: list[AuditResult]) -> None:
    fields = [
        "level", "group", "name", "char_count", "missing_aspects", "weak_aspects",
        "no_previous_rectification", "no_rectification", "third_person_hits",
        "contrast_hits", "too_short", "problem_section_ratio_low", "issues", "file", "source",
    ]
    with OUT_CSV.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        for r in results:
            writer.writerow({
                "level": r.level,
                "group": r.group,
                "name": r.name,
                "char_count": r.char_count,
                "missing_aspects": "、".join(r.missing_aspects),
                "weak_aspects": "；".join(r.weak_aspects),
                "no_previous_rectification": r.no_previous整改,
                "no_rectification": r.no_rectification,
                "third_person_hits": "、".join(r.third_person_hits),
                "contrast_hits": "、".join(r.contrast_hits),
                "too_short": r.too_short,
                "problem_section_ratio_low": r.problem_section_ratio_low,
                "issues": "；".join(r.issues),
                "file": r.file,
                "source": r.source,
            })


def write_report(results: list[AuditResult]) -> None:
    bad = [r for r in results if r.level == "不达标"]
    needs = [r for r in results if r.level == "需修改"]
    ok = [r for r in results if r.level == "基本达标"]

    lines = [
        "# 个人对照检查材料审核报告",
        "",
        f"审核范围：`{ROOT}` 下已转换的个人发言/个人对照检查材料。",
        "",
        "说明：本报告为规则化初审，用于快速定位明显风险；涉及“问题是否深刻、是否见人见事”的判断，建议对命中项再人工复核。",
        "",
        "## 统计",
        "",
        f"- 纳入审核：{len(results)} 份",
        f"- 不达标：{len(bad)} 份",
        f"- 需修改：{len(needs)} 份",
        f"- 基本达标：{len(ok)} 份",
        "",
        "## 不达标名单",
        "",
        "| 支部/单位 | 人员/材料 | 主要问题 | 文件 |",
        "| --- | --- | --- | --- |",
    ]
    for r in bad:
        issue = "<br>".join(r.issues[:5])
        lines.append(f"| {r.group} | {r.name} | {issue} | `{r.file}` |")

    lines.extend(["", "## 需修改名单", "", "| 支部/单位 | 人员/材料 | 主要问题 | 文件 |", "| --- | --- | --- | --- |"])
    for r in needs:
        issue = "<br>".join(r.issues[:5])
        lines.append(f"| {r.group} | {r.name} | {issue} | `{r.file}` |")

    lines.extend(["", "## 基本达标名单", ""])
    for r in ok:
        lines.append(f"- {r.group}：{r.name}")

    OUT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    candidates = []
    for path in ROOT.rglob("*.md"):
        if path.name in {"index.md", "conversion-summary.md", OUT_MD.name}:
            continue
        text = read_text(path)
        if is_personal_material(path, text):
            candidates.append(path)

    results = [audit_file(path) for path in sorted(candidates)]
    write_csv(results)
    write_report(results)
    print(f"audited={len(results)} report={OUT_MD}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
