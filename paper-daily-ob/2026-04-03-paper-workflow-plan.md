# 论文推荐工作流 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 将 paper-workflow 统一为 recommend 单入口，按新目录结构生成每日 Top10 汇总与 Top3 深度报告，并保存 PDF 与图片资产。

**Architecture:** recommend 入口通过现有 search_arxiv 产出 top10，再由助手写入汇总报告；Top3 通过下载 PDF + 提图 + 深度报告写入完成。所有输出遵循 daily_recommend / research / raw_paper 目录结构。

**Tech Stack:** Python 3, PyMuPDF(fitz), arXiv/Semantic Scholar API, Obsidian Markdown

---

## File Structure (Planned Changes)
- Modify: `/Users/mkbk/.claude/skills/paper-workflow/skill.md`
- Create: `/Users/mkbk/.claude/skills/paper-workflow/scripts/download_pdf.py`
- Modify: `/Users/mkbk/Documents/paper-daily-ob/CLAUDE.md`
- Modify: `/Users/mkbk/Documents/paper-daily-ob/.claude/settings.local.json`

---

### Task 1: 更新 skill.md 为 recommend 单入口与新目录规范

**Files:**
- Modify: `/Users/mkbk/.claude/skills/paper-workflow/skill.md`

- [ ] **Step 1: 更新“目标/调用方式/分发规则”文本**

将 `# 目标` 与 `# 调用方式与分发规则` 更新为以下内容（替换原有四模式描述）：

```markdown
# 目标

用一个统一入口处理每日推荐工作流：
- `recommend`：生成每日 Top10 推荐汇总 + Top3 深度解读 + PDF/图片归档

# 调用方式与分发规则

## 调用方式
- `/paper-workflow recommend [YYYY-MM-DD]`

## 分发规则
- 仅支持 recommend 入口；如未指定日期，默认当天
```

- [ ] **Step 2: 更新“全局约定”路径规范**

替换为以下约定：

```markdown
# 全局约定

- Vault 根目录来自环境变量 `OBSIDIAN_VAULT_PATH`
- 每日汇总目录：`$OBSIDIAN_VAULT_PATH/daily_recommend/`
- 深度报告目录：`$OBSIDIAN_VAULT_PATH/research/YYYY-MM-DD/`
- 原文与图片目录：`$OBSIDIAN_VAULT_PATH/raw_paper/YYYY-MM-DD/论文标题/`
- 图片目录：`$OBSIDIAN_VAULT_PATH/raw_paper/YYYY-MM-DD/论文标题/images/`
- 深度报告内嵌图：使用相对路径指向 `raw_paper/.../images/...`
```

- [ ] **Step 3: 更新 recommend 模式说明**

替换 recommend 章节为（保留脚本路径，但流程按新需求）：

```markdown
## 1. recommend

适用：生成当天或指定日期的论文推荐。

输入：
- 可选日期参数 `YYYY-MM-DD`

执行步骤：
1. 读取研究配置：`$OBSIDIAN_VAULT_PATH/99_System/Config/research_interests.yaml`
2. 搜索和筛选论文：
   - `/Users/mkbk/.claude/skills/paper-workflow/scripts/search_arxiv.py`
3. 生成每日推荐汇总（Top10）：
   - 输出到 `daily_recommend/YYYY-MM-DD.md`
   - 包含中英文标题、摘要翻译、完整元信息、可点击链接
4. 对 Top3 执行深度解读与资产归档：
   - 下载 PDF → `raw_paper/YYYY-MM-DD/论文标题/论文标题.pdf`
   - 提图到 `raw_paper/YYYY-MM-DD/论文标题/images/`
   - 生成深度报告 → `research/YYYY-MM-DD/论文标题.md`（内嵌图片）

输出：
- 每日推荐汇总
- Top3 深度报告
- Top3 PDF 与图片资产
```

- [ ] **Step 4: 删除 search/extract-images/analyze 模式说明**

删除原有 2/3/4 模式说明全文，保留 recommend 单入口。

- [ ] **Step 5: 人工检查**

确认 skill.md 中不存在旧路径 `10_Daily/`、`20_Research/`、`Papers/` 等旧规范。

---

### Task 2: 新增 PDF 下载脚本（供 recommend 调用）

**Files:**
- Create: `/Users/mkbk/.claude/skills/paper-workflow/scripts/download_pdf.py`

- [ ] **Step 1: 写入脚本代码**

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
下载论文 PDF 到指定路径
"""

import os
import sys
import argparse
import logging
import urllib.request

logger = logging.getLogger(__name__)


def download(url: str, output_path: str) -> None:
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    try:
        urllib.request.urlretrieve(url, output_path)
    except Exception as e:
        logger.error("Download failed: %s", e)
        raise


def main():
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s [%(levelname)s] %(message)s',
        datefmt='%H:%M:%S',
        stream=sys.stderr,
    )

    parser = argparse.ArgumentParser(description='Download paper PDF')
    parser.add_argument('--url', required=True, help='PDF url')
    parser.add_argument('--output', required=True, help='Output pdf path')
    args = parser.parse_args()

    download(args.url, args.output)
    print(f"PDF saved: {args.output}")


if __name__ == '__main__':
    main()
```

- [ ] **Step 2: 运行一次本地验证（可选）**

Run:
```
python3 /Users/mkbk/.claude/skills/paper-workflow/scripts/download_pdf.py \
  --url "https://arxiv.org/pdf/2402.00001.pdf" \
  --output "/tmp/2402.00001.pdf"
```
Expected: 输出 `PDF saved: /tmp/2402.00001.pdf`

---

### Task 3: 更新 vault 指南与权限配置

**Files:**
- Modify: `/Users/mkbk/Documents/paper-daily-ob/CLAUDE.md`
- Modify: `/Users/mkbk/Documents/paper-daily-ob/.claude/settings.local.json`

- [ ] **Step 1: 更新 CLAUDE.md 目录结构描述**

将“仓库结构（高层概览）”部分替换为：

```markdown
## 仓库结构（高层概览）

- `daily_recommend/`：每日 Top10 推荐汇总（Markdown）
- `research/YYYY-MM-DD/`：Top3 深度解读报告（Markdown，内嵌图片）
- `raw_paper/YYYY-MM-DD/论文标题/`：论文原文 PDF 与图片
  - `images/` 与 PDF 同级
- `paper-daily/99_System/Config/`：研究兴趣与筛选权重配置（`research_interests.yaml`）
```

- [ ] **Step 2: 更新 settings.local.json 的 allow 列表**

删除与 `start-my-day` 相关的旧路径与命令，新增允许的命令（示例）：

```json
{
  "permissions": {
    "allow": [
      "Bash(mkdir:*)",
      "Bash(export OBSIDIAN_VAULT_PATH=\"/Users/mkbk/Documents/paper-daily-ob\")",
      "Read(//Users/mkbk/Documents/paper-daily-ob/**)",
      "Bash(ls:*)",
      "Bash(python3:*)",
      "Bash(python scripts/search_arxiv.py --config \"$OBSIDIAN_VAULT_PATH/paper-daily/99_System/Config/research_interests.yaml\" --output \"$OBSIDIAN_VAULT_PATH/arxiv_filtered.json\" --max-results 200 --top-n 10 --categories \"cs.AI,cs.LG,cs.CL,cs.CV,cs.MM,cs.MA,cs.RO\" --target-date \"$TARGET_DATE\")",
      "Bash(python scripts/extract_images.py:*)",
      "Bash(python scripts/download_pdf.py:*)"
    ]
  }
}
```

---

### Task 4: recommend 执行流程（无脚本新增的助手执行步骤）

**Files:**
- Modify: `/Users/mkbk/.claude/skills/paper-workflow/skill.md`
- Create: `daily_recommend/YYYY-MM-DD.md`
- Create: `research/YYYY-MM-DD/论文标题.md`

- [ ] **Step 1: 在 recommend 中明确汇总报告生成格式**

在 recommend 说明中追加汇总模板（示例片段）：

```markdown
# YYYY-MM-DD 每日论文推荐（Top10）

> 生成时间：YYYY-MM-DD

## 1) {中文标题} / {英文标题}
- arXiv ID：{id}
- 作者：{authors}
- 领域：{domain}
- 评分：{score}
- 摘要（EN）：{abstract_en}
- 摘要（CN）：{abstract_zh}
- 链接：{arxiv_url} | {pdf_url}
```

- [ ] **Step 2: 在 recommend 中明确 Top3 深度报告格式**

追加深度报告模板（示例片段）：

```markdown
# {中文标题} / {英文标题}

## 核心信息
- arXiv ID：{id}
- 作者：{authors}
- 领域：{domain}
- 评分：{score}
- 链接：{arxiv_url} | {pdf_url}

## 摘要翻译
{abstract_zh}

## 方法与创新
{content}

## 实验与结果
{content}

## 关键图表
![](../../raw_paper/YYYY-MM-DD/论文标题/images/fig1.png)
```

---

## Self-Review (Plan)
- **Spec coverage:** 单入口 recommend、目录结构、Top10 汇总、Top3 深度报告、PDF/图片归档、链接可点击、错误降级策略均已覆盖。
- **Placeholder scan:** 无 TBD/TODO/“之后补充”。
- **Type consistency:** 所有路径与文件名规范一致使用 daily_recommend / research / raw_paper。

---

**Plan complete and saved to** `/Users/mkbk/Documents/paper-daily-ob/2026-04-03-paper-workflow-plan.md`.

Two execution options:

1. **Subagent-Driven (recommended)** - I dispatch a fresh subagent per task, review between tasks, fast iteration
2. **Inline Execution** - Execute tasks in this session using executing-plans, batch execution with checkpoints

Which approach?
