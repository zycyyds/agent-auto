---
date: "2026-04-01"
paper_id: "arXiv:2604.00698"
title: "Learning to Hint for Reinforcement Learning"
authors: "Yu Xia, Canwen Xu, Zhewei Yao, Julian McAuley, Yuxiong He"
domain: "强化学习"
tags:
  - 论文笔记
  - 强化学习
created: "2026-04-02"
updated: "2026-04-02"
status: analyzed
---

# Learning to Hint for Reinforcement Learning

## 核心信息
- **论文ID**：arXiv:2604.00698
- **作者**：Yu Xia, Canwen Xu, Zhewei Yao, Julian McAuley, Yuxiong He
- **发布时间**：2026-04-01
- **链接**：[arXiv](http://arxiv.org/abs/2604.00698v1) | [PDF](https://arxiv.org/pdf/2604.00698v1)

![论文图|600](images/fig_transfer_temp.pdf)

## 摘要翻译
Group Relative Policy Optimization (GRPO) is widely used for reinforcement learning with verifiable rewards, but it often suffers from advantage collapse: when all rollouts in a group receive the same reward, the group yields zero relative advantage and thus no learning signal. For example, if a question is too hard for the reasoner, all sampled rollouts can be incorrect and receive zero reward. Recent work addresses this issue by adding hints or auxiliary scaffolds to such hard questions so that the reasoner produces mixed outcomes and recovers a non-zero update. However, existing hints are usually fixed rather than adapted to the current reasoner, and a hint that creates learning signal under the hinted input does not necessarily improve the no-hint policy used at test time. To this end, we propose Hint Learning for Reinforcement Learning (HiLL), a framework that jointly trains a hinter policy and a reasoner policy during RL. For each hard question, the hinter generates hints online conditioned on the current reasoner's incorrect rollout, allowing hint generation to adapt to the reasoner's evolving errors. We further introduce hint reliance, which measures how strongly correct hinted trajectories depend on the hint. We derive a transferability result showing that lower hint reliance implies stronger transfer from hinted success to no-hint success, and we use this result to define a transfer-weighted reward for training the hinter. Therefore, HiLL favors hints that not only recover informative GRPO groups, but also produce signals that are more likely to improve the original no-hint policy. Experiments across multiple benchmarks show that HiLL consistently outperforms GRPO and prior hint-based baselines, demonstrating the value of adaptive and transfer-aware hint learning for RL. The code is available at https://github.com/Andree-9/HiLL.

## 方法概述
- **核心思路**：Group Relative Policy Optimization (GRPO) is widely used for reinforcement learning with verifiable rewards, but it ofte...

## 关键创新
- 从摘要中提炼：Group Relative Policy Optimization (GRPO) is widely used for reinforcement learning with verifiable rewards, but it often suffers from advantage collapse: when ...

## 实验结果
- 从摘要中提炼可能的关键实验结论与性能提升。

## 优势与局限
- **优势**：新方法与性能提升线索来自摘要。
- **局限**：摘要未明确局限，需阅读全文确认。