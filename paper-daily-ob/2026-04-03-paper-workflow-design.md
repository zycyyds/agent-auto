# 论文推荐工作流设计（recommend 入口）

日期：2026-04-03

## 目标
- 仅保留一个入口：`recommend`
- 每日生成：
  - 1 份「10 篇推荐汇总」报告（中英标题、摘要翻译、完整元信息、可点击链接）
  - 3 份「Top3 深度解读」报告（内容完整，内嵌图片）
  - Top3 原文 PDF 与图片归档

## 目录结构（已确认）
```
/Users/mkbk/Documents/paper-daily-ob/
├─ daily_recommend/
│  └─ YYYY-MM-DD.md
├─ research/
│  └─ YYYY-MM-DD/
│     ├─ 论文A.md
│     ├─ 论文B.md
│     └─ 论文C.md
└─ raw_paper/
   └─ YYYY-MM-DD/
      ├─ 论文A/
      │  ├─ 论文A.pdf
      │  └─ images/
      │     ├─ fig1.png
      │     └─ fig2.png
      └─ 论文B/… & 论文C/…
```

## 架构与组件划分
1) **recommend 入口**：统一编排全流程与输出
2) **检索与评分**：arXiv/Semantic Scholar 拉取、过滤、评分、排序、去重
3) **汇总报告生成**：输出 `daily_recommend/YYYY-MM-DD.md`
4) **Top3 深度报告生成**：输出 `research/YYYY-MM-DD/论文X.md`
5) **原文与图片归档**：下载 PDF、从 arXiv source 或 PDF 提图，存放在 `raw_paper` 下
6) **图片嵌入**：Top3 报告内用相对路径嵌入 `raw_paper/.../images/...`

## 数据与文件规范
### 元信息字段（汇总与深度报告均包含）
- arXiv ID
- 标题（中英文）
- 作者
- 发表时间
- 分类/领域
- 摘要（英文原文 + 中文翻译）
- 评分（quality_score）
- 链接：arXiv 页面、PDF（必须可点击、可用）

### 文件命名与路径
- 汇总：`daily_recommend/YYYY-MM-DD.md`
- 深度：`research/YYYY-MM-DD/论文标题.md`
- 原文：`raw_paper/YYYY-MM-DD/论文标题/论文标题.pdf`
- 图片：`raw_paper/YYYY-MM-DD/论文标题/images/figX.png`
- 深度报告内嵌图路径：相对路径指向 `raw_paper` 目录

### 标题文件名规范
- 论文标题中非法字符替换为 `_`
- 同日同名冲突追加短后缀（如 `-2`）

## 流程细节
1) 获取当天推荐 Top10
2) 生成汇总报告（10 篇）
3) 选 Top3
4) 下载 PDF 与提图
5) 生成 Top3 深度报告（嵌图）

## 错误处理策略
- arXiv source 失败：降级到 PDF 图片提取
- PDF 下载失败：Top3 报告保留链接与说明，不阻断全部流程
- 图片提取失败：保留文本报告，注明“图片提取失败”

## 可追溯性
- 每日生成固定目录（按日期）
- 报告内保留原文链接与本地路径信息
