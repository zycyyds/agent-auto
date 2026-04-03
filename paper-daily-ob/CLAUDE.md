# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## 常用命令

未发现可执行代码或构建/测试配置文件（如 package.json、pyproject.toml、Makefile、requirements*.txt）。该仓库看起来是一个 Obsidian 笔记库，当前无可运行的构建、lint、测试命令可提供。

## 仓库结构（高层概览）

- `daily_recommend/`：每日 Top10 推荐汇总（Markdown）
- `research/YYYY-MM-DD/`：Top3 深度解读报告（Markdown，内嵌图片）
- `raw_paper/YYYY-MM-DD/论文标题/`：论文原文 PDF 与图片
  - `images/` 与 PDF 同级
- `paper-daily/99_System/Config/`：研究兴趣与筛选权重配置（research_interests.yaml）
