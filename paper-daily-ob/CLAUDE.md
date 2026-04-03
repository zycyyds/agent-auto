# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## 常用命令

未发现可执行代码或构建/测试配置文件（如 package.json、pyproject.toml、Makefile、requirements*.txt）。该仓库看起来是一个 Obsidian 笔记库，当前无可运行的构建、lint、测试命令可提供。

## 仓库结构（高层概览）

- `paper-daily/10_Daily/`：按日期组织的“论文推荐”每日汇总笔记（Markdown）。
- `paper-daily/20_Research/`：按研究方向分类的论文详细笔记与配套图片索引（`images/index.md`）。
- `paper-daily/99_System/Config/`：研究兴趣与筛选权重配置（`research_interests.yaml`），用于论文筛选/推荐的主题、关键词、权重等。
- `paper-daily/arxiv_filtered.json`：某次筛选结果的论文清单与评分（含时间窗口、论文元数据与得分）。
- `paper-daily/existing_notes_index.json`：现有笔记索引（当前为空）。
- `paper-daily/.obsidian/`：Obsidian 工作区配置。