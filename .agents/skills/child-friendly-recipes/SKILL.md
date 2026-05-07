---
name: child-friendly-recipes
description: Find, write, and optionally push simple, nutritious, kid-friendly Chinese recipes for a 12-year-old who prefers down-to-earth home cooking and does not like fish or seafood. Use when monitoring recent Chinese recipes, writing recipe recommendations into the Obsidian `吃好` folder, pushing the daily recipe note to Feishu, or adjusting recipe selection for child-friendly taste: no fish, shrimp, crab, shellfish, squid, or other seafood; prioritize chicken, beef, pork, eggs, tofu, tomato, potato, and mild sweet-savory or tomato-based dishes.
---

# Child-Friendly Recipes

## Goal

Monitor recent Chinese recipes and write up to 5 new, deduplicated recommendations into the Obsidian folder `吃好`, optimized for a 12-year-old boy who does not like fish or seafood.

## Selection Rules

Prioritize recipes that are:

- Simple: few steps, common ingredients, beginner-friendly.
- Fast: usually 10-35 minutes; allow up to 45 minutes for soup or stew if mostly hands-off.
- Nutritious: include protein plus vegetables or staple-friendly ingredients.
- Child-friendly: tomato, sweet-savory, mild soy sauce, garlic aroma, soft texture, or good for rice/noodles.
- Popular or credible: visible ratings, saves, cooked counts, comments, recent publication, or clear community interaction.
- Recently published when possible; otherwise use recent discovery time and explain that the source is a stable popular recipe/search result.

Exclude:

- Fish, shrimp, crab, shellfish, squid, octopus, seaweed-heavy dishes, fish sauce-forward dishes, and mixed seafood.
- Adult diet-style dishes as the main recommendation, such as plain salads, cold low-fat bowls, bitter greens, sour pickles, or very spicy dishes.
- Recipes that depend on hard-to-buy ingredients or complex restaurant techniques.

Good candidates:

- Tomato scrambled eggs, tomato beef, tomato potato beef soup.
- Garlic chicken wings, potato chicken, teriyaki-style chicken thigh.
- Meat sauce noodles, minced pork steamed egg, meatball soup.
- Tofu with minced meat, egg tofu, tomato tofu.
- Mild curry chicken or potato beef if ingredients are common.

## Workflow

1. Read `$CODEX_HOME/automations/<automation_id>/memory.md` when the automation ID is available.
2. Read existing files under `吃好` and deduplicate by recipe name and source link.
3. Search current Chinese recipe sources if network is available. Prefer Chinese sources such as 下厨房、豆果、美食杰、B站/小红书 recipe pages only when source links are usable.
4. Select at most 5 new recipes using the rules above.
5. Write to `吃好/YYYY-MM-DD 最新菜谱监控.md`. Append if the file exists.
6. Include these fields for every recipe:
   - 菜名
   - 发布时间或发现时间
   - 推荐理由
   - 预计耗时
   - 主要食材
   - 简明步骤
   - 营养亮点
   - 来源链接
   - 筛选依据
7. If Feishu push is requested, send the completed note with `python scripts/send_feishu_recipe.py "吃好/YYYY-MM-DD 最新菜谱监控.md"`. Require `FEISHU_WEBHOOK_URL` or `FEISHU_BOT_WEBHOOK`; use `FEISHU_WEBHOOK_SECRET` when the bot has signature verification enabled.
8. Update automation memory with the run time, selected recipes, exclusions applied, Feishu push status, and any source limitations.

## Output Style

Use concise Chinese. Make the recommendation practical for a parent deciding dinner, not a food blogger review.

Mention seafood exclusion explicitly only when it affects selection or when replacing a seafood recipe.

For Feishu, push a concise text version of the same Obsidian note. Do not store webhook URLs or secrets in files.
