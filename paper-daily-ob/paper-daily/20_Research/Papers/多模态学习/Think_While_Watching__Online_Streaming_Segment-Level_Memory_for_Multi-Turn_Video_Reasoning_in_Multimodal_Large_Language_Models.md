---
date: "2026-03-15"
paper_id: "arXiv:2603.11896"
title: "Think While Watching: Online Streaming Segment-Level Memory for Multi-Turn Video Reasoning in Multimodal Large Language Models"
authors: "Lu Wang, Zhuoran Jin, Yupu Hao, Yubo Chen, Kang Liu, Yulong Ao, Jun Zhao"
domain: "多模态学习"
tags:
  - 论文笔记
  - 多模态学习
  - 流式视频理解
  - 在线推理
  - 多轮交互
  - 段级记忆
quality_score: "9.0/10"
related_papers:
  - [[20_Research/Papers/大语言模型/Abductive_Reasoning_Syllogistic_LLM]]
created: "2026-03-15"
updated: "2026-03-15"
status: analyzed
---

# Think While Watching: Online Streaming Segment-Level Memory for Multi-Turn Video Reasoning in Multimodal Large Language Models

## 核心信息
- **论文 ID**: arXiv:2603.11896
- **作者**: Lu Wang, Zhuoran Jin, Yupu Hao, Yubo Chen, Kang Liu, Yulong Ao, Jun Zhao
- **机构**: 待补充
- **发布时间**: 2026-03-12
- **会议/期刊**: arXiv preprint
- **链接**: [arXiv](https://arxiv.org/abs/2603.11896) | [PDF](https://arxiv.org/pdf/2603.11896)
- **代码**: [GitHub](https://github.com/wl666hhh/Think_While_Watching/)

## 摘要翻译

### 英文摘要
Multimodal large language models (MLLMs) have shown strong performance on offline video understanding, but most are limited to offline inference or have weak online reasoning, making multi-turn interaction over continuously arriving video streams difficult. Existing streaming methods typically use an interleaved perception-generation paradigm, which prevents concurrent perception and generation and leads to early memory decay as streams grow, hurting long-range dependency modeling. We propose Think While Watching, a memory-anchored streaming video reasoning framework that preserves continuous segment-level memory during multi-turn interaction. We build a three-stage, multi-round chain-of-thought dataset and adopt a stage-matched training strategy, while enforcing strict causality through a segment-level streaming causal mask and positional encoding. During inference, we introduce an efficient pipeline that overlaps watching and thinking and selects the best attention backend. Under both single-round and multi-round streaming input protocols, our method achieves strong results. Built on Qwen3-VL, it improves single-round accuracy by 2.6% on StreamingBench and by 3.79% on OVO-Bench. In the multi-round setting, it maintains performance while reducing output tokens by 56%.

### 中文翻译
多模态大语言模型（MLLMs）在离线视频理解方面表现出色，但大多数局限于离线推理或在线推理能力弱，难以对连续到达的视频流进行多轮交互。现有的流式方法通常采用交错感知 - 生成范式，这阻碍了并发感知和生成，并导致随着流增长出现早期记忆衰减，损害长距离依赖建模。我们提出了"边看边想"（Think While Watching），这是一个基于记忆的流式视频推理框架，在多轮交互过程中保持连续的段级记忆。我们构建了一个三阶段、多轮次的思维链数据集，并采用阶段匹配的训练策略，同时通过段级流式因果掩码和位置编码强制实施严格的因果性。在推理过程中，我们引入了一个高效的流水线，将观看和思考重叠，并选择最佳的注意力后端。在单轮和多轮流式输入协议下，我们的方法都取得了强劲的结果。基于 Qwen3-VL 构建，它在 StreamingBench 上将单轮准确率提高了 2.6%，在 OVO-Bench 上提高了 3.79%。在多轮设置中，它在保持性能的同时将输出 token 减少了 56%。

### 核心要点提炼
- **研究背景**: 现有 MLLM 在流式视频理解和多轮交互方面能力有限
- **研究动机**: 交错感知 - 生成范式阻碍并发处理，导致记忆衰减和长距离依赖建模困难
- **核心方法**: 提出段级记忆锚定的流式推理框架，实现"边看边想"
- **主要结果**: StreamingBench +2.6%，OVO-Bench +3.79%，多轮设置输出 token 减少 56%
- **研究意义**: 为流式视频理解提供了高效的在线推理框架

## 研究背景与动机

### 领域现状
多模态大语言模型在视频理解领域取得了显著进展：
1. **离线视频理解**: MLLMs 在处理完整视频上表现优秀
2. **流式视频理解**: 新兴研究方向，需要处理连续到达的视频帧

### 现有方法的局限性
- **离线方法的局限**:
  - 需要完整视频才能开始推理
  - 无法应对实时视频流场景
  - 不支持多轮交互

- **现有流式方法的问题**:
  - **交错感知 - 生成范式**: 感知和生成不能并发进行
  - **早期记忆衰减**: 随着视频流增长，早期帧的记忆逐渐消失
  - **长距离依赖建模困难**: 难以捕捉视频中的长期时间关系

### 研究动机
- 需要一种能够并发感知和生成的框架
- 需要在多轮交互中保持连续的记忆
- 需要高效处理长视频的长距离依赖

## 研究问题

### 核心研究问题
1. 如何在流式视频输入过程中实现并发感知和推理？
2. 如何在多轮交互中保持连续的段级记忆，避免记忆衰减？
3. 如何高效处理长视频中的长距离时间依赖？
4. 如何在保持性能的同时减少计算开销？

## 方法概述

### 核心思想
"边看边想"（Think While Watching）的核心思想：
- **段级记忆锚定**: 将视频分成段，每段保持独立的记忆表示
- **并发处理**: 观看新帧的同时思考已看内容
- **因果性保证**: 通过段级流式因果掩码确保只依赖历史信息

### 方法框架

#### 整体架构

![注意力机制图](多模态学习/Think_While_Watching__Online_Streaming_Segment-Level_Memory_for_Multi-Turn_Video_Reasoning_in_Multimodal_Large_Language_Models/images/attention_page1)

> 图 1: Think While Watching 的注意力机制架构

#### 核心组件

1. **段级记忆模块 (Segment-Level Memory)**
   - 将连续视频流分成逻辑段
   - 每段维护独立的记忆表示
   - 支持跨段查询和检索

2. **流式因果掩码 (Streaming Causal Mask)**
   - 确保每个时刻只能关注历史信息
   - 强制实施时间因果性
   - 支持动态长度的视频流

3. **段级位置编码 (Segment-Level Positional Encoding)**
   - 编码段内和段间的位置信息
   - 支持长距离依赖建模
   - 保持时间连续性

4. **高效推理流水线 (Efficient Inference Pipeline)**
   - 重叠观看（感知）和思考（生成）过程
   - 动态选择最佳注意力后端
   - 优化 token 生成效率

### 三阶段训练策略

1. **阶段一**: 基础视觉 - 语言对齐
2. **阶段二**: 段级记忆学习
3. **阶段三**: 多轮交互优化

### 关键创新
1. **段级记忆锚定**: 首次在多轮交互中保持连续的段级记忆
2. **并发感知 - 生成**: 打破交错范式，实现高效流水线
3. **严格因果性保证**: 通过专门设计的掩码和位置编码
4. **三阶段训练**: 阶段匹配的训练策略

## 实验结果

### 数据集

#### 自建数据集
- **三阶段、多轮次思维链数据集**:
  - 包含多个推理难度级别
  - 覆盖多种视频类型
  - 支持单轮和多轮评估协议

#### 评估基准
- **StreamingBench**: 流式视频理解基准
- **OVO-Bench**: 在线视频推理基准

### 实验设置
- **基线模型**: Qwen3-VL
- **对比方法**: 现有流式视频理解方法
- **评估指标**: 准确率、输出 token 数、延迟

### 主要结果

#### 单轮设置结果
| 方法 | StreamingBench | OVO-Bench |
|------|---------------|-----------|
| 基线 (Qwen3-VL) | baseline | baseline |
| **Think While Watching** | **+2.6%** | **+3.79%** |

#### 多轮设置结果
| 指标 | 改进 |
|------|------|
| 性能 | 保持 |
| 输出 token | **减少 56%** |

### 延迟分析

![延迟对比](多模态学习/Think_While_Watching__Online_Streaming_Segment-Level_Memory_for_Multi-Turn_Video_Reasoning_in_Multimodal_Large_Language_Models/images/latency_page1)

> 图 2: Think While Watching 与基线方法的延迟对比

### 单轮 CoT 分布

![单轮 CoT 分布](多模态学习/Think_While_Watching__Online_Streaming_Segment-Level_Memory_for_Multi-Turn_Video_Reasoning_in_Multimodal_Large_Language_Models/images/single_cot_distribution_page1)

> 图 3: 单轮设置下思维链长度分布

### 多轮 CoT 分布

![多轮 CoT 分布](多模态学习/Think_While_Watching__Online_Streaming_Segment-Level_Memory_for_Multi-Turn_Video_Reasoning_in_Multimodal_Large_Language_Models/images/multi_turn_cot_distribution_page1)

> 图 4: 多轮设置下思维链长度分布

### 长距离 CoT 分布

![长距离 CoT 分布](多模态学习/Think_While_Watching__Online_Streaming_Segment-Level_Memory_for_Multi-Turn_Video_Reasoning_in_Multimodal_Large_Language_Models/images/long_range_cot_distribution_page1)

> 图 5: 长距离依赖任务中的思维链分布

### F1/F3/Error 分析

![F1 指标](多模态学习/Think_While_Watching__Online_Streaming_Segment-Level_Memory_for_Multi-Turn_Video_Reasoning_in_Multimodal_Large_Language_Models/images/F1_page1)

![F3 指标](多模态学习/Think_While_Watching__Online_Streaming_Segment-Level_Memory_for_Multi-Turn_Video_Reasoning_in_Multimodal_Large_Language_Models/images/F3_page1)

![错误分析](多模态学习/Think_While_Watching__Online_Streaming_Segment-Level_Memory_for_Multi-Turn_Video_Reasoning_in_Multimodal_Large_Language_Models/images/Error_page1)

### 案例研究

![案例研究](多模态学习/Think_While_Watching__Online_Streaming_Segment-Level_Memory_for_Multi-Turn_Video_Reasoning_in_Multimodal_Large_Language_Models/images/case_study_page1)

> 图 6: Think While Watching 的成功案例分析

### 结果分析
- **单轮提升显著**: 在两个基准上都取得明显提升
- **多轮效率高**: 在保持性能的同时大幅减少 token 使用
- **长距离依赖**: 段级记忆有效支持长视频理解
- **并发优势**: 高效流水线降低了整体延迟

## 深度分析

### 研究价值

#### 理论贡献
- **段级记忆理论**: 提出了连续视频流记忆的新范式
- **因果性形式化**: 为流式视频推理建立了严格的因果框架
- **并发处理模型**: 打破了感知 - 生成交错的传统范式

#### 实际应用价值
- **实时监控**: 适用于安防监控、工业检测等实时场景
- **视频直播**: 支持直播内容的实时分析和交互
- **视频会议**: 支持会议内容的实时摘要和问答
- **自动驾驶**: 支持连续视觉流的实时推理

#### 领域影响
- 推动了 MLLM 从离线向在线的范式转变
- 为流式多模态理解建立了新的基准
- 启发了更多关于并发处理的研究

### 优势
1. **并发处理**: 观看和思考可以同时进行，提高效率
2. **记忆保持**: 段级记忆有效防止早期记忆衰减
3. **因果保证**: 严格的因果性确保推理可靠性
4. **高效 token 使用**: 多轮设置下减少 56% 的 token

### 局限性
1. **段划分依赖**: 性能可能依赖于段划分的质量
2. **计算复杂度**: 段级记忆可能增加计算开销
3. **实时性限制**: 虽然高效，但仍有延迟优化空间

### 适用场景
- **实时视频分析**: 监控、直播等需要即时响应的场景
- **长视频理解**: 需要捕捉长距离依赖的任务
- **多轮交互**: 视频问答、对话式分析等场景
- **资源受限**: 需要在性能和效率间权衡的场景

### 不适用场景
- **离线批处理**: 如果不需要实时性，离线方法可能更简单
- **短视频**: 对于很短的视频，优势不明显
- **单帧任务**: 不涉及时间维度的任务

## 与相关论文对比

### 相关视频理解论文
- **关系类型**: 相关 - 视频理解方法
- **差异**: 本文专注流式在线推理，其他可能关注离线理解
- **改进**: 首次实现段级记忆锚定的并发处理

## 技术路线定位

### 所属技术路线
本文属于**多模态视频理解**技术路线，主要关注**流式在线推理**。

### 技术路线发展历程
```
单帧理解 → 离线视频 → 在线流式 → 并发处理 → Think While Watching
   ↑         ↑         ↑          ↑              ↑
图像问答   视频问答   实时推理   交错范式      段级记忆并发
```

### 本文在技术路线中的位置
- **承上**: 继承了在线流式推理的研究方向
- **启下**: 开辟了并发处理和段级记忆的新方向
- **关键节点**: 首次实现真正的"边看边想"

## 未来工作建议

### 作者建议的未来工作
1. **自适应段划分**: 学习最优的段划分策略
2. **更长视频**: 扩展到小时级视频理解
3. **多模态扩展**: 整合音频等多模态信息
4. **实时部署**: 优化在实际系统中的部署

### 基于分析的未来方向
1. **动态记忆管理**: 根据重要性动态分配记忆资源
2. **跨视频推理**: 支持多个相关视频的联合推理
3. **增量学习**: 在流式过程中持续更新模型
4. **人机协作**: 支持人类在流式过程中的实时干预

## 我的综合评价

### 价值评分

#### 总体评分
**9.0/10** - 在流式视频理解方向取得重要突破，兼具理论创新和实用价值

#### 分项评分

| 评分维度 | 分数 | 评分理由 |
|----------|------|----------|
| 创新性 | 9/10 | 段级记忆和并发处理是原创性贡献 |
| 技术质量 | 9/10 | 方法设计严谨，因果性保证充分 |
| 实验充分性 | 9/10 | 在多个基准上验证，分析全面 |
| 写作质量 | 8/10 | 组织清晰，但部分细节可更详尽 |
| 实用性 | 9/10 | 直接适用于实时监控等场景 |

### 重点关注

#### 值得关注的技术点
- 段级记忆的实现细节
- 流式因果掩码的设计
- 并发流水线的调度策略

#### 需要深入理解的部分
- 三阶段训练的具体配置
- 注意力后端选择策略
- 段划分对性能的影响

## 我的笔记

%% 用户可以在这里添加个人阅读笔记 %%

## 相关论文

### 直接相关
- 视频理解相关论文待补充

### 背景相关
- [[Abductive Reasoning Syllogistic LLM]] - 推理能力

### 后续工作
- 待补充

## 外部资源
- **代码仓库**: [GitHub](https://github.com/wl666hhh/Think_While_Watching/)

> [!tip] 关键启示
> "边看边想"代表了流式视频理解的未来方向：并发处理、段级记忆、高效推理

> [!warning] 注意事项
> - 段划分质量可能显著影响性能
> - 实时部署需要额外的工程优化
> - 长视频理解仍是开放挑战

> [!success] 推荐指数
> ⭐⭐⭐⭐⭐ 强烈推荐给视频理解和多模态研究者！这是流式推理的重要里程碑
