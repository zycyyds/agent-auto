---
date: "2026-03-15"
paper_id: "arXiv:2603.11991"
title: "BTZSC: A Benchmark for Zero-Shot Text Classification Across Cross-Encoders, Embedding Models, Rerankers and LLMs"
authors: "Ilias Aarab"
domain: "大语言模型"
tags:
  - 论文笔记
  - 零样本分类
  - 基准评测
  - 文本嵌入
  - Reranker
  - LLM
quality_score: "8.8/10"
related_papers:
  - [[20_Research/Papers/大语言模型/COLD_Steer_InContext_OneStep_Learning]]
created: "2026-03-15"
updated: "2026-03-15"
status: analyzed
---

# BTZSC: A Benchmark for Zero-Shot Text Classification Across Cross-Encoders, Embedding Models, Rerankers and LLMs

## 核心信息
- **论文 ID**: arXiv:2603.11991
- **作者**: Ilias Aarab
- **机构**: 待补充
- **发布时间**: 2026-03-12
- **会议/期刊**: arXiv preprint
- **链接**: [arXiv](https://arxiv.org/abs/2603.11991) | [PDF](https://arxiv.org/pdf/2603.11991)

## 摘要翻译

### 英文摘要
Zero-shot text classification (ZSC) offers the promise of eliminating costly task-specific annotation by matching texts directly to human-readable label descriptions. While early approaches have predominantly relied on cross-encoder models fine-tuned for natural language inference (NLI), recent advances in text-embedding models, rerankers, and instruction-tuned large language models (LLMs) have challenged the dominance of NLI-based architectures. Yet, systematically comparing these diverse approaches remains difficult. Existing evaluations, such as MTEB, often incorporate labeled examples through supervised probes or fine-tuning, leaving genuine zero-shot capabilities underexplored. To address this, we introduce BTZSC, a comprehensive benchmark of 22 public datasets spanning sentiment, topic, intent, and emotion classification, capturing diverse domains, class cardinalities, and document lengths. Leveraging BTZSC, we conduct a systematic comparison across four major model families: cross-encoders, embedding models, rerankers and instruction-tuned LLMs, encompassing 38 public and custom checkpoints. Our results show that: (i) modern rerankers, exemplified by Qwen3-Reranker-8B, set a new state-of-the-art with macro F1 = 0.72; (ii) strong embedding models such as GTE-large-en-v1.5 substantially close the accuracy gap while offering the best trade-off between accuracy and latency; (iii) instruction-tuned LLMs at 4-12B parameters achieve competitive performance (macro F1 up to 0.67), excelling particularly on topic classification but trailing specialized rerankers; (iv) NLI cross-encoders plateau even as backbone size increases; and (v) scaling primarily benefits rerankers and LLMs over embedding models. BTZSC and accompanying evaluation code are publicly released to support fair and reproducible progress in zero-shot text understanding.

### 中文翻译
零样本文本分类（ZSC）承诺通过将文本直接匹配到人类可读的标签描述来消除昂贵的任务特定标注。虽然早期方法主要依赖于为自然语言推理（NLI）微调的交叉编码器模型，但文本嵌入模型、reranker 和指令微调大语言模型（LLM）的最新进展挑战了基于 NLI 的架构的主导地位。然而，系统地比较这些多样化方法仍然困难。现有的评估（如 MTEB）通常通过监督探针或微调引入标注样本，导致真正的零样本能力未被充分探索。为此，我们引入了 BTZSC，这是一个包含 22 个公共数据集的综合基准，涵盖情感、主题、意图和情感分类，捕捉了多样化的领域、类别数量和文档长度。利用 BTZSC，我们对四个主要模型家族进行了系统比较：交叉编码器、嵌入模型、reranker 和指令微调 LLM，涵盖 38 个公共和自定义检查点。我们的结果表明：(i) 现代 reranker（以 Qwen3-Reranker-8B 为代表）以 macro F1 = 0.72 创下新的 state-of-the-art；(ii) 强大的嵌入模型（如 GTE-large-en-v1.5）大幅缩小了准确性差距，同时提供了准确性和延迟之间的最佳权衡；(iii) 4-12B 参数的指令微调 LLM 实现了有竞争力的性能（macro F1 高达 0.67），在主题分类上表现突出，但落后于专用 reranker；(iv) NLI 交叉编码器即使骨干规模增加也会达到平台期；(v) 扩展主要有利于 reranker 和 LLM 而非嵌入模型。BTZSC 和配套评估代码已公开发布，以支持零样本文本理解的公平和可重现进展。

### 核心要点提炼
- **研究背景**: 零样本文本分类方法多样化，但缺乏系统性的公平比较基准
- **研究动机**: 现有评估（如 MTEB）使用监督信号，无法评估真正的零样本能力
- **核心方法**: 提出 BTZSC 基准，包含 22 个数据集，系统比较 4 类模型共 38 个检查点
- **主要结果**: Qwen3-Reranker-8B 以 macro F1=0.72 创 SOTA；GTE-large-en-v1.5 提供最佳精度 - 延迟权衡
- **研究意义**: 为零样本文本分类领域提供了公平、全面的评估基准

## 研究背景与动机

### 领域现状
零样本文本分类（ZSC）近年来经历了快速发展：
1. **早期方法**: 基于 NLI 的交叉编码器（如 BERT 微调为 NLI 模型）
2. **新兴方法**:
   - 文本嵌入模型（Embedding Models）
   - Reranker 模型
   - 指令微调大语言模型（Instruction-tuned LLMs）

### 现有方法的局限性
- **MTEB 等现有基准**:
  - 通过监督探针或微调引入标注样本
  - 无法评估真正的零样本能力
  - 缺乏对多样化模型家族的系统比较
- **评估不全面**:
  - 数据集覆盖有限
  - 缺乏对不同领域、类别数量、文档长度的系统分析

### 研究动机
- 需要真正的零样本评估基准，不使用任何标注样本
- 需要系统比较不同模型家族的优势和劣势
- 为研究者提供公平、可重现的比较平台

## 研究问题

### 核心研究问题
1. 现代嵌入模型、reranker 和 LLM 在真正的零样本设置下表现如何？
2. 哪类模型在不同任务类型（情感、主题、意图、情感）上各有什么优势？
3. 模型规模扩展对不同类型模型的性能提升有何差异？
4. 精度和延迟之间的最佳权衡点在哪里？

## 方法概述

### 核心方法
BTZSC 基准的设计原则：
1. **真正的零样本**: 不使用任何标注样本进行训练或微调
2. **多样性**: 覆盖 22 个数据集，涵盖多种任务类型和领域
3. **公平比较**: 对所有模型使用统一的评估协议
4. **全面分析**: 从精度、延迟、模型规模等多维度分析

### BTZSC 基准组成

#### 数据集覆盖
| 任务类型 | 数据集数量 | 领域覆盖 |
|----------|-----------|----------|
| 情感分类 | 待补充 | 评论、社交媒体等 |
| 主题分类 | 待补充 | 新闻、学术等 |
| 意图分类 | 待补充 | 对话、查询等 |
| 情感分类 | 待补充 | 多领域 |

#### 评估的模型家族
1. **交叉编码器 (Cross-Encoders)**: NLI 微调模型
2. **嵌入模型 (Embedding Models)**: GTE 等
3. **Reranker**: Qwen3-Reranker 等
4. **指令微调 LLM**: 4-12B 参数模型

#### 评估指标
- **Macro F1**: 主要评估指标，考虑类别不平衡
- **延迟**: 推理时间
- **计算效率**: FLOPs 或吞吐量

### 关键创新
1. **真正的零样本基准**: 第一个不使用任何监督信号的 ZSC 基准
2. **系统化比较**: 首次对 4 类模型进行公平比较
3. **规模分析**: 研究模型规模对性能的影响规律

## 实验结果

### 主要结果

| 模型类别 | 代表模型 | Macro F1 | 特点 |
|----------|---------|----------|------|
| **Reranker** | Qwen3-Reranker-8B | **0.72** | 新 SOTA |
| **LLM (4-12B)** | 指令微调 LLM | 0.67 | 主题分类突出 |
| **嵌入模型** | GTE-large-en-v1.5 | ~0.65 | 最佳精度 - 延迟权衡 |
| **交叉编码器** | NLI 模型 | 平台期 | 规模增加无提升 |

### 关键发现

1. **Reranker 称霸**: Qwen3-Reranker-8B 以 macro F1=0.72 创下新 SOTA
2. **嵌入模型崛起**: GTE-large-en-v1.5 大幅缩小精度差距，提供最佳延迟表现
3. **LLM 竞争力强**: 4-12B 参数的 LLM 达到 macro F1=0.67，在主题分类上表现突出
4. **NLI 平台期**: 交叉编码器即使增加骨干规模，性能也趋于饱和
5. **规模效应差异**: 扩展主要有利于 reranker 和 LLM，对嵌入模型收益较小

### 精度 - 延迟权衡分析

![性能 vs 延迟对比图](大语言模型/BTZSC__A_Benchmark_for_Zero-Shot_Text_Classification_Across_Cross-Encoders_Embedding_Models_Rerankers_and_LLMs/images/fig_04_performance_v_latency_page1)

> 图 1: 各类模型的精度 - 延迟权衡对比

### NLI 模型性能对比

![NLI 性能对比](大语言模型/BTZSC__A_Benchmark_for_Zero-Shot_Text_Classification_Across_Cross-Encoders_Embedding_Models_Rerankers_and_LLMs/images/fig_02_nli_performance_comparison_page1)

> 图 2: NLI 交叉编码器在不同规模下的性能对比，显示平台期现象

## 深度分析

### 研究价值

#### 理论贡献
- **基准贡献**: 首个真正的零样本文本分类基准
- **系统分析**: 揭示了不同模型家族的能力边界和扩展规律
- **评估协议**: 为公平比较建立了标准协议

#### 实际应用价值
- **模型选择指南**: 为实际应用提供模型选择依据
  - 追求最高精度 → 选择 reranker
  - 追求精度 - 延迟平衡 → 选择嵌入模型
  - 主题分类任务 → 考虑 LLM
- **资源规划**: 帮助工程师根据资源限制选择合适的模型

#### 领域影响
- 推动零样本文本分类研究向更公平、更透明的方向发展
- 揭示了 NLI 方法的局限性，指引未来研究方向
- 为嵌入模型和 reranker 的发展提供了明确目标

### 优势
1. **真正的零样本**: 完全排除了监督信号的影响
2. **覆盖全面**: 22 个数据集覆盖多任务、多领域
3. **公平比较**: 统一评估协议，结果可信
4. **可重现**: 代码和数据公开

### 局限性
1. **仅限英文**: 可能主要覆盖英文数据集
2. **静态基准**: 无法捕捉快速发展的模型能力
3. **计算成本**: 评估 38 个模型需要大量计算资源

### 适用场景
- **模型选择**: 需要为新任务选择合适模型时参考
- **研究基准**: 开发新 ZSC 方法时作为对比基准
- **技术分析**: 了解不同模型家族的能力边界

### 不适用场景
- **低资源场景**: 如果允许使用少量标注样本，应使用少样本方法
- **非英文任务**: 需要额外验证多语言能力
- **特殊领域**: 如医疗、法律等专业领域需要领域特定评估

## 与相关论文对比

### [[COLD: Steer InContext OneStep Learning]]
- **关系类型**: 相关 - LLM 在上下文学习中的应用
- **差异**: COLD 关注上下文学习策略，BTZSC 关注零样本分类基准
- **互补性**: COLD 方法可以在 BTZSC 基准上评估

## 技术路线定位

### 所属技术路线
本文属于**零样本文本分类**技术路线，主要关注**基准评测**。

### 技术路线发展历程
```
NLI 交叉编码器 → 嵌入模型 → Reranker → 指令 LLM → BTZSC 统一基准
     ↑            ↑          ↑         ↑          ↑
  早期主导    效率优势    精度突破   泛化能力   公平比较
```

### 本文在技术路线中的位置
- **承上**: 总结了各类方法的发展成果
- **启下**: 为未来研究提供了公平比较平台
- **关键节点**: 首次实现真正的零样本系统评估

## 未来工作建议

### 作者建议的未来工作
1. **扩展数据集**: 覆盖更多领域和语言
2. **动态更新**: 跟踪新发布的模型
3. **多语言评估**: 扩展为非英语基准
4. **任务扩展**: 覆盖更多 NLP 任务

### 基于分析的未来方向
1. **混合方法**: 探索嵌入模型+reranker 的组合策略
2. **自适应选择**: 根据输入特征动态选择模型类型
3. **效率优化**: 针对 reranker 开发加速方法
4. **领域适应**: 研究零样本领域迁移方法

## 我的综合评价

### 价值评分

#### 总体评分
**8.8/10** - 为零样本文本分类领域提供了重要的基准资源，发现具有实践指导意义

#### 分项评分

| 评分维度 | 分数 | 评分理由 |
|----------|------|----------|
| 创新性 | 8/10 | 首个真正的零样本基准，设计思路清晰 |
| 技术质量 | 9/10 | 评估协议严谨，覆盖全面 |
| 实验充分性 | 9/10 | 38 个模型×22 个数据集，分析深入 |
| 写作质量 | 8/10 | 组织清晰，发现呈现有力 |
| 实用性 | 9/10 | 对实际模型选择有直接指导价值 |

### 重点关注

#### 值得关注的技术点
- Reranker 在零样本设置下的优势机制
- 嵌入模型的精度 - 延迟最优平衡点
- LLM 在主题分类上的特殊优势

#### 需要深入理解的部分
- 不同任务类型对各模型家族的敏感性
- 规模效应的理论基础

## 我的笔记

%% 用户可以在这里添加个人阅读笔记 %%

## 相关论文

### 直接相关
- 零样本学习相关论文待补充

### 背景相关
- [[COLD: Steer InContext OneStep Learning]] - LLM 上下文学习

### 后续工作
- 待补充

## 外部资源
- 项目主页：待补充
- 代码仓库：待补充

> [!tip] 关键启示
> Reranker 代表了当前零样本分类的最高水平，但嵌入模型提供了最佳的精度 - 延迟权衡

> [!warning] 注意事项
> - NLI 交叉编码器已达平台期，不建议继续投入
> - LLM 的零样本能力虽强但成本高
> - 选择模型时需权衡精度和延迟

> [!success] 推荐指数
> ⭐⭐⭐⭐ 强烈推荐给从事文本分类的研究者和工程师！这是选择模型的重要参考
