import json
import os

# 读取所有JSON文件
json_dir = 'output/json'
json_files = [f for f in os.listdir(json_dir) if f.startswith('个人评分-') and f.endswith('.json')]

data_list = []
for json_file in json_files:
    try:
        with open(os.path.join(json_dir, json_file), 'r', encoding='utf-8') as f:
            data = json.load(f)
            data_list.append(data)
    except Exception as e:
        print(f"Error reading {json_file}: {e}")

# 按最终得分降序排序
data_list.sort(key=lambda x: x.get('最终得分', 0), reverse=True)

print(f"成功读取 {len(data_list)} 份材料")

# 生成Markdown汇总表
md_lines = []
md_lines.append("# 2025年度组织生活会个人材料评分汇总表\n")
md_lines.append("**评分日期**: 2026-03-02\n")
md_lines.append(f"**材料总数**: {len(data_list)}份\n\n")
md_lines.append("---\n\n")
md_lines.append("## 评分排名\n\n")

# 表头
md_lines.append("| 排名 | 姓名 | 部门 | 维度一 | 维度二 | 维度三 | 维度四 | 维度五 | 维度六 | 维度七 | 维度八 | 加权总分 | 硬伤项 | 最终得分 |\n")
md_lines.append("|------|------|------|--------|--------|--------|--------|--------|--------|--------|--------|----------|--------|----------|\n")

# 数据行
for idx, data in enumerate(data_list, 1):
    name = data.get('姓名', '未知')
    dept = data.get('部门', '未知')
    
    vp = data.get('维度评分', {})
    v1 = vp.get('维度一_结构完整性', {}).get('得分', 0)
    v2 = vp.get('维度二_问题查摆', {}).get('综合得分', 0)
    v3 = vp.get('维度三_原因剖析', {}).get('得分', 0)
    v4 = vp.get('维度四_整改措施', {}).get('得分', 0)
    v5 = vp.get('维度五_篇幅结构', {}).get('得分', 0)
    v6 = vp.get('维度六_需报告事项', {}).get('得分', 0)
    v7 = vp.get('维度七_上年度整改', {}).get('得分', 0)
    v8 = vp.get('维度八_文字规范', {}).get('得分', 0)
    
    total = data.get('加权总分', 0)
    issues = ', '.join(data.get('硬伤项', [])) if data.get('硬伤项') else '无'
    final = data.get('最终得分', 0)
    
    md_lines.append(f"| {idx} | {name} | {dept} | {v1} | {v2} | {v3} | {v4} | {v5} | {v6} | {v7} | {v8} | {total:.2f} | {issues} | {final} |\n")

# 统计信息
md_lines.append("\n---\n\n")
md_lines.append("## 统计信息\n\n")

scores = [d.get('最终得分', 0) for d in data_list]
md_lines.append(f"- **最高分**: {max(scores)}分\n")
md_lines.append(f"- **最低分**: {min(scores)}分\n")
md_lines.append(f"- **平均分**: {sum(scores)/len(scores):.2f}分\n")

# 分数段分布
score_ranges = {
    '4.5-5.0分': len([s for s in scores if 4.5 <= s <= 5.0]),
    '4.0-4.4分': len([s for s in scores if 4.0 <= s < 4.5]),
    '3.5-3.9分': len([s for s in scores if 3.5 <= s < 4.0]),
    '3.0-3.4分': len([s for s in scores if 3.0 <= s < 3.5]),
    '3.0分以下': len([s for s in scores if s < 3.0])
}

md_lines.append("\n### 分数段分布\n\n")
for range_name, count in score_ranges.items():
    md_lines.append(f"- {range_name}: {count}份\n")

# 评分说明
md_lines.append("\n---\n\n")
md_lines.append("## 评分说明\n\n")
md_lines.append("本次评分严格按照《2025年度组织生活会 个人发言提纲 评分标准（Rubric）》执行，从8个维度进行综合评价：\n\n")
md_lines.append("1. **维度一：结构完整性**（权重10%）- 检查7个必备要素和6个方面是否齐全\n")
md_lines.append("2. **维度二：问题查摆质量**（权重30%）- 包含4个子项：第一人称视角、禁止先扬后抑、见人见事、问题深度\n")
md_lines.append("3. **维度三：原因剖析质量**（权重15%）- 从思想根源深挖\n")
md_lines.append("4. **维度四：整改措施质量**（权重15%）- 与问题对应，措施具体可操作\n")
md_lines.append("5. **维度五：篇幅结构合理性**（权重10%）- 问题查摆+原因剖析占比\n")
md_lines.append("6. **维度六：需要说明和报告的事项**（权重5%）- 配偶子女、房产、约谈函询等\n")
md_lines.append("7. **维度七：上年度整改及八项规定/巡视巡察**（权重10%）- 逐项报告\n")
md_lines.append("8. **维度八：文字规范性**（权重5%）- 基础分5分，扣分项\n")

# 写入文件
output_path = 'output/个人材料评分汇总.md'
with open(output_path, 'w', encoding='utf-8') as f:
    f.writelines(md_lines)

print(f"汇总表已生成: {output_path}")

