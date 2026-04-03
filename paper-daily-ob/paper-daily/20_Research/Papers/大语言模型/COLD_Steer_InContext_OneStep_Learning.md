---
date: "2026-03-09"
paper_id: "arXiv:2603.06495"
title: "COLD-Steer: Steering Large Language Models via In-Context One-step Learning Dynamics"
authors: "Kartik Sharma, Rakshit S. Trivedi"
domain: "大语言模型"
tags:
  - 论文笔记
  - LLM
  - Activation-Steering
  - In-Context-Learning
  - Efficient-Control
  - Pluralistic-Alignment
quality_score: "8.8/10"
created: "2026-03-09"
updated: "2026-03-09"
status: analyzed
---

# COLD-Steer: Steering Large Language Models via In-Context One-step Learning Dynamics

## 核心信息
- **论文 ID**：arXiv:2603.06495
- **作者**：Kartik Sharma (Georgia Tech), Rakshit S. Trivedi (MIT)
- **机构**：Georgia Institute of Technology, Massachusetts Institute of Technology
- **发布时间**：2026-03-06
- **会议/期刊**：ICLR 2026 投稿
- **链接**：[arXiv](https://arxiv.org/abs/2603.06495) | [PDF](https://arxiv.org/pdf/2603.06495.pdf)
- **代码**：[GitHub](https://github.com/Ksartik/cold-steer)

## 摘要翻译

### 英文摘要
Activation steering methods enable inference-time control of large language model (LLM) behavior without retraining, but current approaches face a fundamental trade-off: sample-efficient methods suboptimally capture steering signals from labeled examples, while methods that better extract these signals require hundreds to thousands of examples. We introduce COLD-Steer, a training-free framework that steers LLM activations by approximating the representational changes that would result from gradient descent on in-context examples. Our key insight is that the effect of fine-tuning on a small set of examples can be efficiently approximated at inference time without actual parameter updates. We formalize this through two complementary approaches: (i) a unit kernel approximation method that updates the activations directly using gradients with respect to them, normalized across examples, and (ii) a finite-difference approximation requiring only two forward passes regardless of example count. Experiments across a variety of steering tasks and benchmarks demonstrate that COLD-Steer achieves upto 95% steering effectiveness while using 50 times fewer samples compared to the best baseline. COLD-Steer facilitates accommodating diverse perspectives without extensive demonstration data, which we validate through our experiments on pluralistic alignment tasks.

### 中文翻译
激活导向方法能够在不需重新训练的情况下实现大语言模型（LLM）行为的推理时控制，但当前方法面临一个基本权衡：样本高效的方法从标注示例中捕获导向信号的效果不佳，而能更好提取这些信号的方法则需要数百到数千个示例。我们介绍了 COLD-Steer，一个无需训练的框架，通过近似在上下文示例上梯度下降将产生的表示变化来导向 LLM 激活。我们的关键洞察是：在少量示例上微调的效果可以在推理时高效近似，而无需实际参数更新。我们通过两种互补方法形式化这一洞察：(i) 单元核近似方法，使用关于激活的梯度直接更新激活，在示例间归一化；(ii) 有限差分近似方法，无论示例数量多少都只需两次前向传播。在多种导向任务和基准测试上的实验表明，COLD-Steer 实现了高达 95% 的导向有效性，同时使用的样本比最佳基线少 50 倍。COLD-Steer 能够在不需要大量演示数据的情况下适应多样化视角，我们在多元对齐任务上的实验验证了这一点。

### 核心要点提炼
- **研究背景**：激活导向方法热门，但现有方法在样本效率和导向效果间存在权衡
- **研究动机**：人类从数十个示例就能学习行为转变，而 LLM 需要数百到数千示例
- **核心方法**：提出 COLD-Steer，通过近似在上下文学习动态来导向模型，无需训练
- **主要结果**：在多个导向任务上达到 95% 有效性，使用 50 倍更少样本
- **研究意义**：为多元对齐和自适应模型控制提供新方法

## 研究背景与动机

### 领域现状
LLM 导向（Steering）方法旨在控制模型行为而不重新训练，主要包括：
- **提示工程**：通过精心设计的提示控制输出，但需要大量手动工作
- **激活导向**：在推理时干预中间激活，直接修改概念表示
- **参数微调**：训练少量参数实现导向，但需要大量数据和训练

### 现有方法的局限性
1. **对比方法（如 CAA、DiffMean）**：
   - 仅需正负示例对，样本效率较高
   - 但依赖激活差异信号，导向效果有限
   - 无法处理仅正示例的场景

2. **参数调优方法（如 ReFT、BiPO）**：
   - 使用梯度信号，导向效果好
   - 但需要 250-1000 个示例训练
   - 需要多轮训练和超参数调优

3. **根本问题**：现有方法将导向视为静态优化问题，寻找对所有输入都有效的单一方向，而非利用模型自身的学习机制

### 研究动机
1. **人类学习的启示**：人类从数十个示例就能掌握行为转变，LLM 应该也能做到
2. **学习动态的可分析性**：近期研究表明微调对表示的影响遵循可分析的模式
3. **核心洞察**：模拟学习而非实际训练——计算模型如何从少量示例学习，直接应用该变换

## 研究问题

### 核心研究问题
1. 能否在不训练的情况下，从少量示例中提取有效的导向信号？
2. 如何近似微调对中间表示的影响？
3. COLD-Steer 能否在多种导向任务上超越现有方法？

## 方法概述

### 核心思想
COLD-Steer 的核心思想是：**最优导向函数应产生与梯度下降相同的激活变化效果**。即，通过模拟模型从少量示例学习的过程，直接计算激活变化，而非实际更新参数。

### 方法框架

#### 整体架构

```
┌─────────────────────────────────────────────────────────────────┐
│                    COLD-Steer Pipeline                          │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  In-Context Examples                                            │
│  (正示例/负示例对 or 仅正示例)                                    │
│         ↓                                                       │
│  ┌─────────────────────────────────────┐                        │
│  │   计算学习动态 (Learning Dynamics)   │                        │
│  │                                     │                        │
│  │   Option 1: Kernel Approximation    │                        │
│  │   - 单元核近似                       │                        │
│  │   - N 次反向传播 + 1 次前向传播        │                        │
│  │                                     │                        │
│  │   Option 2: Finite Difference       │                        │
│  │   - 有限差分近似                     │                        │
│  │   - N 次反向传播 + 2 次前向传播        │                        │
│  └─────────────────────────────────────┘                        │
│         ↓                                                       │
│  计算激活变化 ΔZ*(x)                                            │
│         ↓                                                       │
│  应用到新输入的中间激活                                          │
│         ↓                                                       │
│  导向后的输出                                                   │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

#### 推理形式对比

**问题形式化**：
给定 in-context 示例 {($\tilde{x}_i$, $\tilde{y}_i$)}, 寻找导向函数 ΔZ*(x) 使得：

$$\Delta Z^*(x) = \arg\min_{\Delta Z(x)} \sum_{i=1}^{N} L(M(\tilde{x}_i; \theta | \text{do}(Z(\tilde{x}_i) = Z(\tilde{x}_i) + \Delta Z(\tilde{x}_i))), \tilde{y}_i)$$

**关键洞察**：
最优导向应近似梯度下降的效果：

$$\Delta Z^*(x; \theta) \approx -\eta/N \sum_{i=1}^{N} \nabla_{\theta} Z(x; \theta) \nabla_{\theta} L(M(\tilde{x}_i), \tilde{y}_i)$$

#### 两种近似方法

**方法 1: COLD-Kernel-Steer（核近似）**

使用核技巧近似梯度乘积：

$$\Delta Z^{(\kappa)}(x) = -\eta/N \sum_{i=1}^{N} \kappa(Z(x), Z(\tilde{x}_i)) \nabla_{Z} L(M(\tilde{x}_i), \tilde{y}_i)|_{Z(\tilde{x}_i)}$$

**单元核简化**（论文发现效果很好）：
$$\kappa(f_i, f_j) = 1$$

这导致简单的平均梯度向量更新。

**方法 2: COLD-FD-Steer（有限差分近似）**

使用有限差分定义梯度：

$$\Delta Z^{(fd)}(x) = -\eta/(\varepsilon \cdot N) (Z(x; \theta + \varepsilon \sum_{i} \nabla_{\theta} L(M(\tilde{x}_i), \tilde{y}_i)) - Z(x; \theta))$$

**关键优势**：只需 2 次前向传播（参数为θ和θ+ε∑∇），无需对新输入进行反向传播。

### 复杂度分析

| 方法 | 示例处理时间 | 示例处理空间 | 推理时间 | 推理空间 |
|------|-------------|-------------|---------|---------|
| 对比方法 | O(2·N·T_fwd) | O(d) | O(T_fwd + d) | O(N·d) |
| 参数调优 | O(N_e·N·T_bwd) | O(|G_bwd|) | O(T_fwd + L_M·d) | O(L_M·d) |
| COLD-Kernel | O(N·T_bwd) | O(|G_bwd|) | O(T_fwd + N·d) | O(N·d) |
| COLD-FD | O(N·T_bwd) | O(|G_bwd|) | O(2·T_fwd) | O(|θ|) |

### 与现有方法的统一

**Corollary 1**: DiffMean (CAA) 等价于 COLD-Kernel 使用特定损失函数

**Corollary 2**: RepE 和 ICV 近似 COLD-Kernel，假设加性并取主成分

## 实验结果

### 实验设置

#### 数据集
- **CAA**: 7 个导向任务（coordinate-ais, corrig-HH, hallucination, myopic-rew, refusal, surv-inst, sycophancy）
- **BiPO**: 4 个导向任务
- **OpinionsQA**: 多元对齐任务（人口统计学条件分布）

#### 基线方法
- **对比方法**: DiffMean, DiffMeanPW, DiffMeanProj, ICV
- **参数调优**: ReFT(mlp), ReFT(vec)/BiPO
- **提示控制**: Base, Base(ICL)

#### 评估模型
- Llama-2-7b-hf, Llama-2-7b-chat-hf
- Qwen-2.5-7B-Instruct
- Mistral-7B-Instruct-v0.1
- Gemma-2-9B

#### 评估指标
- **行为选择**: 准确率（正确选项 logit 更高）
- **行为生成**: LLM-as-a-judge 评分
- **分布导向**: KL 散度，TV 距离

### 主要结果

#### 行为选择准确率（CAA 数据集，50 样本）

| 方法 | coordinate | corrig-HH | hallucination | refusal | 平均排名 |
|------|-----------|-----------|---------------|---------|---------|
| **Llama-2-7b-chat-hf** |
| Base | 0.28 | 0.62 | 0.70 | 0.62 | 5.14 |
| DiffMean | 0.52 | 0.82 | 0.86 | 0.74 | 4.00 |
| ReFT(vec) | 0.48 | 0.62 | 0.70 | 0.72 | 3.29 |
| **COLD-FD** | **0.90** | **0.86** | **0.96** | **0.98** | **2.00** |
| COLD-Kernel | 0.28 | 0.62 | 0.70 | 0.64 | 4.43 |
| **Llama-2-7b-hf** |
| Base | 0.52 | 0.58 | 0.68 | 0.38 | 2.00 |
| DiffMean | 0.50 | 0.62 | 0.58 | 0.38 | 4.43 |
| **COLD-FD** | 0.52 | 0.58 | **0.78** | **0.58** | **1.29** |
| **Qwen-2.5-7B-Instruct** |
| Base | 0.02 | 0.38 | 0.32 | 0.90 | 3.43 |
| DiffMean | 0.02 | 0.48 | 0.36 | 0.90 | 2.57 |
| **COLD-FD** | **0.98** | **0.98** | **0.94** | **0.94** | **1.00** |

#### 样本效率对比

COLD-Steer 使用 50 倍更少样本达到相同导向效果：
- **基线需要**: 250-1000 样本
- **COLD 需要**: 5-20 样本

#### 多元对齐结果

在 OpinionsQA 上，COLD-FD 显著降低了 KL 散度和 TV 距离，能够有效适应不同人口统计学群体的观点分布。

### 结果分析

1. **COLD-FD 表现最佳**：在所有模型和任务上 consistently 最优
2. **支持正负示例对和仅正示例**：对比方法只能使用正负对
3. **样本效率极高**：5-20 样本就能达到基线 250-1000 样本的效果
4. **跨模型泛化**：在 Llama、Qwen、Mistral、Gemma 上都有效

## 深度分析

### 研究价值评估

#### 理论贡献
- **统一框架**：将现有对比方法（DiffMean、RepE、ICV）统一为 COLD 的特例
- **学习动态视角**：从学习动态角度重新理解激活导向
- **无需训练导向**：证明无需参数更新即可实现有效导向

#### 实际应用价值
- **多元对齐**：适应不同用户群体的价值观和偏好
- **安全过滤**：实时应用安全过滤（"我无法提供危险活动指导"）
- **风格控制**：控制输出风格（技术性 vs 简化解释）
- **低资源场景**：在标注数据稀缺的场景下也能应用

#### 领域影响
- **短期**：提供新的激活导向工具，被研究和应用采用
- **中期**：推动多元对齐和个性化 AI 发展
- **长期**：改变模型部署和微调范式

### 方法优势详解

#### 优势 1：样本效率
- **描述**：仅需 5-20 样本就能达到良好效果
- **技术基础**：利用模型已有的 in-context 学习能力
- **实验验证**：在 7 个 CAA 任务上验证
- **对比分析**：比 ReFT 少 50 倍样本

#### 优势 2：无需训练
- **描述**：完全 training-free，推理时直接计算
- **技术基础**：有限差分和核近似
- **实验验证**：推理时间与基线相当
- **对比分析**：省去训练时间和计算资源

#### 优势 3：灵活性
- **描述**：支持正负对、仅正、分布导向多种模式
- **技术基础**：通用损失函数框架
- **实验验证**：在 OpinionsQA 上验证分布导向
- **对比分析**：对比方法仅支持正负对

### 局限性分析

#### 局限 1：计算复杂度
- **描述**：COLD-FD 需要存储完整参数空间 O(|θ|)
- **表现**：对于 7B 模型需要约 14GB 额外内存
- **原因**：有限差分需要 perturbed 参数
- **影响**：在资源受限设备上可能不适用
- **解决方案**：论文提到可忽略小变化参数（<4% 显著变化）

#### 局限 2：核近似效果不稳定
- **描述**：COLD-Kernel 在某些模型上效果不佳
- **表现**：在 Qwen 上几乎无改进
- **原因**：单元核假设在某些架构下不成立
- **影响**：需要根据模型选择方法
- **解决方案**：优先使用 COLD-FD

#### 局限 3：超参数选择
- **描述**：需要选择导向层和 multiplier
- **表现**：η和 l 需要验证集调优
- **原因**：不同任务最优层可能不同
- **影响**：增加部署复杂度
- **解决方案**：默认值η=1, l∈{15,30} 效果稳健

### 场景分析

#### 适用场景
- **多元对齐应用**：需要适应不同用户群体价值观
- **低资源导向**：标注数据稀缺的场景
- **实时控制**：需要快速适应新导向目标
- **研究探索**：分析模型表示和概念编码

#### 不适用场景
- **极大规模模型**：存储 O(|θ|) 不现实
- **严格延迟要求**：需要 2 次前向传播可能过慢
- **永久性导向**：如需固定导向，训练方法更稳定

## 与相关论文对比

### [[Wu et al., 2024]] - ReFT: Representation Fine-tuning

#### 基本信息
- **作者**：Wu et al.
- **发表时间**：2024
- **核心方法**：训练 MLP 或向量变换表示

#### 对比
| 对比维度 | ReFT | COLD-Steer |
|----------|------|-----------|
| 是否需要训练 | 是（2 epochs） | 否 |
| 样本需求 | 250-1000 | 5-20 |
| 推理时间 | O(T_fwd) | O(2·T_fwd) |
| 导向效果 | 良好 | 更优 |

### [[Panickssery et al., 2023]] - CAA: Contrastive Activation Addition

#### 基本信息
- **作者**：Panickssery et al.
- **发表时间**：2023
- **核心方法**：添加正负示例激活均值差异

#### 对比
| 对比维度 | CAA | COLD-Steer |
|----------|-----|-----------|
| 示例类型 | 仅正负对 | 正负对/仅正/分布 |
| 理论解释 | 启发式 | 统一学习动态框架 |
| 导向效果 | 中等 | 更优 |

### [[Zou et al., 2023]] - RepE: Representation Engineering

#### 基本信息
- **作者**：Zou et al.
- **发表时间**：2023
- **核心方法**：使用主成分分析激活差异

#### 对比
| 对比维度 | RepE | COLD-Steer |
|----------|------|-----------|
| 方法复杂度 | 低 | 中 |
| 理论联系 | COLD 近似特例 | 统一框架 |

## 技术路线定位

### 所属技术路线
本文属于**激活导向（Activation Steering）**技术路线，核心特点：
- 在推理时干预中间激活
- 无需修改模型参数
- 基于线性表示假设

### 技术路线发展历程
```
Activation Addition (2023) → CAA (2023) → RepE/ICV (2023) → ReFT (2024) → COLD-Steer (2026)
```

### 本文在技术路线中的位置
- **承上**：统一对比方法为 COLD 特例
- **启下**：为学习动态导向奠定基础
- **关键节点**：首次实现 training-free 且样本高效的导向

## 未来工作建议

### 作者建议的未来工作
1. **降低空间复杂度**：探索更高效的参数扰动存储
2. **扩展任务类型**：测试更复杂的导向场景
3. **理论研究**：深入分析核近似为何有效

### 基于分析的未来方向
1. **自适应层选择**：根据输入动态选择导向层
2. **多导向组合**：同时应用多个导向信号
3. **因果分析**：研究导向对模型内部计算的影响

## 我的综合评价

### 价值评分

#### 总体评分
**8.8/10** - 高质量的激活导向研究，显著提升样本效率

#### 分项评分

| 评分维度 | 分数 | 评分理由 |
|----------|------|----------|
| 创新性 | 9/10 | 提出学习动态导向新视角，统一现有方法 |
| 技术质量 | 9/10 | 理论推导严谨，两种近似方法互补 |
| 实验充分性 | 9/10 | 测试 5 个模型、11 个任务，对比全面 |
| 写作质量 | 9/10 | 论文结构清晰，论证充分 |
| 实用性 | 8/10 | training-free 易部署，但空间复杂度较高 |

### 重点关注

#### 值得关注的技术点
1. **有限差分近似**：仅用 2 次前向传播避免反向传播
2. **单元核有效性**：简单平均梯度向量效果意外地好
3. **与对比方法的统一**：DiffMean/RepE/ICV 都是 COLD 特例

#### 需要深入理解的部分
1. **学习动态理论基础**：Neural Tangent Kernel 与导向的关系
2. **线性表示假设**：为何单元核在某些模型上失效

## 我的笔记

%% 用户可以在这里添加个人阅读笔记 %%

## 相关论文

### 直接相关
- [[Wu et al., 2024]] - ReFT: 参数调优导向基线
- [[Panickssery et al., 2023]] - CAA: 对比激活导向
- [[Zou et al., 2023]] - RepE: 表示工程

### 背景相关
- [[Elhage et al., 2021]] - Transformer 可解释性数学框架
- [[Santurkar et al., 2023]] - 多元对齐问题定义

## 外部资源
- 代码：https://github.com/Ksartik/cold-steer

> [!tip] 关键启示
> 将导向重新定义为"模拟学习"而非"静态优化"，是从数百样本到数十样本的关键突破。

> [!warning] 注意事项
> - COLD-FD 需要 O(|θ|) 额外空间，7B 模型约需 14GB
> - COLD-Kernel 在不同模型上效果不稳定，优先使用 COLD-FD

> [!success] 推荐指数
> ⭐⭐⭐⭐⭐ 强烈推荐！这是激活导向领域的重大进展，显著提升样本效率且无需训练。
