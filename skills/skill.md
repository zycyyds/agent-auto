---
name: paper-workflow
description: Use when users request daily paper recommendations or specify a date for recommendations
allowed-tools: Read, Write, Bash, Grep, Glob, WebFetch
---
You are the unified Paper Workflow skill for OrbitOS.

# 目标

用一个统一入口处理每日推荐工作流：
- `recommend`：生成每日 Top 10 推荐汇总 + Top 3 深度解读 + PDF/图片归档

# 调用方式与分发规则

## 调用方式
- `/paper-workflow recommend [YYYY-MM-DD]`

## 分发规则
- 仅支持 recommend 入口；如未指定日期，默认当天

# 全局约定

- Vault 根目录：`OBSIDIAN_VAULT_PATH`
- 每日汇总：`$OBSIDIAN_VAULT_PATH/daily_recommend/`
- 深度报告：`$OBSIDIAN_VAULT_PATH/research/YYYY-MM-DD/`
- 原文与图片：`$OBSIDIAN_VAULT_PATH/raw_paper/YYYY-MM-DD/论文标题/`
- 图片目录：`$OBSIDIAN_VAULT_PATH/raw_paper/YYYY-MM-DD/论文标题/images/`
- 深度报告内嵌图：相对路径指向 raw_paper

# 环境依赖

- Python 3
- PyYAML（读取研究兴趣配置）
- PyMuPDF（fitz，用于图片提取）
- 网络连接（访问 arXiv / Semantic Scholar）

# 模式说明

## recommend

适用：生成当天或指定日期的每日推荐与归档。

输入：
- 可选日期参数 `YYYY-MM-DD`

执行步骤：
1. 读取 `research_interests.yaml`
2. 调用 `scripts/search_arxiv.py`
3. 生成 `daily_recommend/YYYY-MM-DD.md`（中英标题、摘要翻译、完整元信息、可点击链接）
4. 对 Top 3 论文：
   - 下载 PDF → `raw_paper/YYYY-MM-DD/论文标题/论文.pdf`
   - 提取图片 → `raw_paper/YYYY-MM-DD/论文标题/images/`
   - 生成深度报告 → `research/YYYY-MM-DD/论文标题.md`（内嵌图片）

输出：
- 每日推荐汇总
- Top 3 深度报告（含内嵌图）
- PDF 与图片归档

模板：

Top 10 汇总模板片段：
```
# YYYY-MM-DD 每日论文推荐（Top 10）
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

Top 3 深度报告模板片段（含图片相对路径示例）：
```
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

示例：
- `/paper-workflow recommend`
- `/paper-workflow recommend 2026-04-02`

# 统一规则

- 深度报告内嵌图使用指向 raw_paper 的相对路径
- 所有新增内容遵循全局约定目录

