---
date: "2026-04-01"
paper_id: "arXiv:2604.00890"
title: "Beyond Symbolic Solving: Multi Chain-of-Thought Voting for Geometric Reasoning in Large Language Models"
authors: "Md. Abu Bakor Siddique, Shahrin Hossain, Sadman Ahmed Siam, Syed Rifat Raiyan, Hasan Mahmud, Md Kamrul Hasan"
domain: "大语言模型"
tags:
  - 论文笔记
  - 大语言模型
created: "2026-04-02"
updated: "2026-04-02"
status: analyzed
---

# Beyond Symbolic Solving: Multi Chain-of-Thought Voting for Geometric Reasoning in Large Language Models

## 核心信息
- **论文ID**：arXiv:2604.00890
- **作者**：Md. Abu Bakor Siddique, Shahrin Hossain, Sadman Ahmed Siam, Syed Rifat Raiyan, Hasan Mahmud, Md Kamrul Hasan
- **发布时间**：2026-04-01
- **链接**：[arXiv](http://arxiv.org/abs/2604.00890v1) | [PDF](https://arxiv.org/pdf/2604.00890v1)

![论文图|600](images/cot_scaling2_2.pdf)

## 摘要翻译
Geometric Problem Solving (GPS) remains at the heart of enhancing mathematical reasoning in large language models because it requires the combination of diagrammatic understanding, symbolic manipulation and logical inference. In existing literature, researchers have chiefly focused on synchronising the diagram descriptions with text literals and solving the problem. In this vein, they have either taken a neural, symbolic or neuro-symbolic approach. But this solves only the first two of the requirements, namely diagrammatic understanding and symbolic manipulation, while leaving logical inference underdeveloped. The logical inference is often limited to one chain-of-thought (CoT). To address this weakness in hitherto existing models, this paper proposes MARS-GPS, that generates multiple parallel reasoning rollouts augmented with Python code execution for numerical verification, ranks them using token-level entropy as a confidence signal, and aggregates answers through a multi-stage voting and self-verification pipeline. Empirical results show that MARS-GPS with 8 parallel rollouts achieves 88.8% on Geometry3K, a nearly +11% improvement over the prior state-of-the-art, with accuracy scaling consistently as the number of rollouts increases from 1 to 16 (+6.0% on ablation subset). We provide our code and data in an anonymous repository: https://anonymous.4open.science/r/MARS-GPS-DE55.

## 方法概述
- **核心思路**：Geometric Problem Solving (GPS) remains at the heart of enhancing mathematical reasoning in large language models becaus...

## 关键创新
- 从摘要中提炼：Geometric Problem Solving (GPS) remains at the heart of enhancing mathematical reasoning in large language models because it requires the combination of diagram...

## 实验结果
- 从摘要中提炼可能的关键实验结论与性能提升。

## 优势与局限
- **优势**：新方法与性能提升线索来自摘要。
- **局限**：摘要未明确局限，需阅读全文确认。