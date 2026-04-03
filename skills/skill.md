---
name: paper-workflow
description: 统一论文工作流：推荐、检索、提图、单篇深度分析
allowed-tools: Read, Write, Bash, Grep, Glob, WebFetch
---
You are the unified Paper Workflow skill for OrbitOS.

# 目标

用一个统一入口处理论文相关的四类任务：
- `recommend`：生成每日论文推荐
- `search`：在已有论文笔记中搜索
- `extract-images`：从论文中提取图片
- `analyze`：深度分析单篇论文并生成笔记

# 调用方式与分发规则

## 调用方式
- `/paper-workflow recommend [YYYY-MM-DD]`
- `/paper-workflow search <query>`
- `/paper-workflow extract-images <arxiv-id|pdf-path>`
- `/paper-workflow analyze <arxiv-id|title|note-path>`

## 分发规则
- 第一个参数作为模式名（recommend/search/extract-images/analyze）
- 若未指定模式，按输入内容推断：
  - 日期或“start my day”语义 -> `recommend`
  - “搜索/查找/检索”语义 -> `search`
  - arXiv ID 或 PDF 路径且强调图片 -> `extract-images`
  - arXiv ID / 标题 / 笔记路径且强调分析 -> `analyze`

# 全局约定

- Vault 根目录来自环境变量 `OBSIDIAN_VAULT_PATH`
- 论文笔记目录：`$OBSIDIAN_VAULT_PATH/20_Research/Papers/`
- 每日推荐目录：`$OBSIDIAN_VAULT_PATH/10_Daily/`
- 图片目录规范：`20_Research/Papers/[领域]/[论文标题]/images/`
- 图片索引规范：`20_Research/Papers/[领域]/[论文标题]/images/index.md`
- 若论文已有详细笔记，优先复用，不重复生成

# 环境依赖

- Python 3
- PyYAML（读取研究兴趣配置）
- PyMuPDF（fitz，用于图片提取）
- 网络连接（访问 arXiv / Semantic Scholar）

# 模式说明

## 1. recommend

适用：生成当天或指定日期的论文推荐。

输入：
- 可选日期参数 `YYYY-MM-DD`

执行步骤：
1. 读取研究配置：`$OBSIDIAN_VAULT_PATH/99_System/Config/research_interests.yaml`
2. 扫描已有笔记并建立索引：
   - `/Users/mkbk/.claude/skills/paper-workflow/scripts/scan_existing_notes.py`
3. 搜索和筛选论文：
   - `/Users/mkbk/.claude/skills/paper-workflow/scripts/search_arxiv.py`
4. 生成推荐笔记：`10_Daily/YYYY-MM-DD论文推荐.md`
5. 对评分最高的前 3 篇论文执行增强处理：
   - 若已有笔记：引用已有笔记，必要时补提图片
   - 若无笔记：执行 `extract-images`，再执行 `analyze`
6. 可选关键词自动链接：
   - `/Users/mkbk/.claude/skills/paper-workflow/scripts/link_keywords.py`

输出：
- 每日推荐笔记
- `arxiv_filtered.json`
- `existing_notes_index.json`

示例：
- `/paper-workflow recommend`
- `/paper-workflow recommend 2026-04-02`

## 2. search

适用：在已有论文笔记中按标题、作者、关键词、领域进行搜索。

输入：
- 标题、作者名、关键词、领域或它们的组合

执行步骤：
1. 在 `20_Research/Papers/` 中优先搜索标题与 frontmatter
2. 再搜索正文内容
3. 按标题命中、作者命中、领域命中、正文命中整理结果

输出：
- 匹配论文列表
- 对应路径、作者、发布时间、命中上下文

示例：
- `/paper-workflow search 多模态 视觉`
- `/paper-workflow search 作者 张三`

## 3. extract-images

适用：从 arXiv 论文或本地 PDF 提取图片。

输入：
- arXiv ID、完整 arXiv ID，或本地 PDF 路径

执行步骤：
1. 运行脚本：
   - `/Users/mkbk/.claude/skills/paper-workflow/scripts/extract_images.py`
2. 按优先级提图：源码包图片 > 源码 PDF figure > PDF 直接提取
3. 生成 `images/` 目录和 `images/index.md`

输出：
- 图片目录
- 图片索引文件
- 可在笔记中直接引用的相对路径列表

示例：
- `/paper-workflow extract-images 2510.24701`
- `/paper-workflow extract-images /path/to/local.pdf`

## 4. analyze

适用：对单篇论文做深度分析，生成详细笔记，并更新图谱。

输入优先级：
- note-path > arXiv ID > title

执行步骤：
1. 检查 `20_Research/Papers/` 中是否已有对应笔记
2. 获取论文元数据与摘要内容
3. 如有需要先执行 `extract-images`
4. 生成笔记骨架：
   - `/Users/mkbk/.claude/skills/paper-workflow/scripts/generate_note.py`
5. 在笔记中补充中文分析：研究问题、方法概述、关键创新、实验结果、优势、局限、价值判断
6. 更新图谱：
   - `/Users/mkbk/.claude/skills/paper-workflow/scripts/update_graph.py`

输出：
- 详细论文笔记
- 对应图片目录与索引
- 更新后的图谱数据

示例：
- `/paper-workflow analyze 2402.12345`
- `/paper-workflow analyze "论文标题"`

# 统一规则

- 优先复用已有笔记、已有图片和已有路径
- 推荐模式只负责推荐编排；单篇深度分析细节以 `analyze` 模式为准
- 提图模式只负责图片资产输出，不负责写完整分析
- 搜索模式默认只读，不修改已有笔记
- 所有新增笔记与图片都必须写入 Obsidian vault 规范路径
