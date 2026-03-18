# 评分任务指令

你是一名党建工作评审专家，负责按照Rubric对组织生活会材料进行标准化评分。

## 工作要求

1. 严格按照Rubric中每个维度的评分标准逐项打分
2. 每个维度给出分值和1-2句扣分理由
3. 按公式计算加权总分
4. 检查是否触发硬伤项
5. 给出3条最关键的整改建议（按优先级排序）
6. 输出标准化JSON格式结果

## 输出格式要求

` ` `json
{
  "文件名": "",
  "材料类型": "班子/个人",
  "支部名称": "",
  "姓名": "",
  "维度评分": {
    "维度一_结构完整性": { "分值": 0, "理由": "" },
    "维度二_问题查摆质量": {
      "子项A": { "分值": 0, "理由": "" },
      "子项B": { "分值": 0, "理由": "" },
      "子项C": { "分值": 0, "理由": "" },
      "子项D": { "分值": 0, "理由": "" },
      "综合分": 0
    },
    "维度三_原因剖析质量": { "分值": 0, "理由": "" },
    "维度四_整改措施质量": { "分值": 0, "理由": "" },
    "维度五_上年度整改": { "分值": 0, "理由": "" },
    "维度六_八项规定及巡视巡察": { "分值": 0, "理由": "" },
    "维度七_文字规范性": { "分值": 0, "理由": "" }
  },
  "加权总分": 0,
  "硬伤项": [],
  "最终得分": 0,
  "整改建议": ["", "", ""]
}

### 批量执行脚本

在项目根目录创建 `batch-review.sh`：

` ` `bash
#!/bin/bash

RUBRIC_BANZI="rubric/rubric-班子材料.md"
RUBRIC_GEREN="rubric/rubric-个人材料.md"
OUTPUT_DIR="output"
TIMESTAMP=$(date +%Y%m%d_%H%M%S)

# 评分班子材料
echo "=== 开始评分班子材料 ==="
for file in materials/班子/*.md; do
  filename=$(basename "$file" .md)
  echo "正在评分: $filename"
  
  claude -p "
你是党建工作评审专家。请严格按照以下Rubric对材料进行评分。

## Rubric评分标准：
$(cat "$RUBRIC_BANZI")

## 评分prompt模板：
$(cat prompt-template.md)

## 待评材料：
$(cat "$file")

请严格按照输出格式要求，输出JSON评分结果。
" > "$OUTPUT_DIR/${filename}_评分_${TIMESTAMP}.json"
  
  echo "完成: $filename"
done

# 评分个人材料
echo "=== 开始评分个人材料 ==="
for file in materials/个人/*.md; do
  filename=$(basename "$file" .md)
  echo "正在评分: $filename"
  
  claude -p "
你是党建工作评审专家。请严格按照以下Rubric对材料进行评分。

## Rubric评分标准：
$(cat "$RUBRIC_GEREN")

## 评分prompt模板：
$(cat prompt-template.md)

## 待评材料：
$(cat "$file")

请严格按照输出格式要求，输出JSON评分结果。
" > "$OUTPUT_DIR/${filename}_评分_${TIMESTAMP}.json"
  
  echo "完成: $filename"
done

echo "=== 全部评分完成，结果在 $OUTPUT_DIR 目录 ==="
bash
chmod +x batch-review.sh
