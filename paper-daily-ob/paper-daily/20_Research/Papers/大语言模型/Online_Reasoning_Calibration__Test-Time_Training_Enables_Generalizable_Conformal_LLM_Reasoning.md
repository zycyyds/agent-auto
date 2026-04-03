---
date: "2026-04-01"
paper_id: "arXiv:2604.01170"
title: "Online Reasoning Calibration: Test-Time Training Enables Generalizable Conformal LLM Reasoning"
authors: "Cai Zhou, Zekai Wang, Menghua Wu, Qianyu Julie Zhu, Flora C. Shi, Chenyu Wang"
domain: "大语言模型"
tags:
  - 论文笔记
  - 大语言模型
created: "2026-04-02"
updated: "2026-04-02"
status: analyzed
---

# Online Reasoning Calibration: Test-Time Training Enables Generalizable Conformal LLM Reasoning

## 核心信息
- **论文ID**：arXiv:2604.01170
- **作者**：Cai Zhou, Zekai Wang, Menghua Wu, Qianyu Julie Zhu, Flora C. Shi, Chenyu Wang
- **发布时间**：2026-04-01
- **链接**：[arXiv](http://arxiv.org/abs/2604.01170v1) | [PDF](https://arxiv.org/pdf/2604.01170v1)

![论文图|600](images/trajectory_page1.png)

## 摘要翻译
While test-time scaling has enabled large language models to solve highly difficult tasks, state-of-the-art results come at exorbitant compute costs. These inefficiencies can be attributed to the miscalibration of post-trained language models, and the lack of calibration in popular sampling techniques. Here, we present Online Reasoning Calibration (ORCA), a framework for calibrating the sampling process that draws upon conformal prediction and test-time training. Specifically, we introduce a meta-learning procedure that updates the calibration module for each input. This allows us to provide valid confidence estimates under distributional shift, e.g. in thought patterns that occur across different stages of reasoning, or in prompt distributions between model development and deployment. ORCA not only provides theoretical guarantees on conformal risks, but also empirically shows higher efficiency and generalization across different reasoning tasks. At risk level $δ=0.1$, ORCA improves Qwen2.5-32B efficiency on in-distribution tasks with savings up to 47.5% with supervised labels and 40.7% with self-consistency labels. Under zero-shot out-of-domain settings, it improves MATH-500 savings from 24.8% of the static calibration baseline to 67.0% while maintaining a low empirical error rate, and the same trend holds across model families and downstream benchmarks. Our code is publicly available at https://github.com/wzekai99/ORCA.

## 方法概述
- **核心思路**：While test-time scaling has enabled large language models to solve highly difficult tasks, state-of-the-art results come...

## 关键创新
- 从摘要中提炼：While test-time scaling has enabled large language models to solve highly difficult tasks, state-of-the-art results come at exorbitant compute costs. These inef...

## 实验结果
- 从摘要中提炼可能的关键实验结论与性能提升。

## 优势与局限
- **优势**：新方法与性能提升线索来自摘要。
- **局限**：摘要未明确局限，需阅读全文确认。