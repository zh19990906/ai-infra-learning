# Algorithm Engineer Roadmap

面向有 Python 工程经验的开发者，用 6 个月建立机器学习、深度学习、Transformer/LLM、项目工程化与面试能力。

## 目标

完成后你应该能够：

- 独立完成标准机器学习项目：数据处理 → 训练 → 验证 → 评估
- 使用 PyTorch 手写训练循环并理解反向传播
- 理解 Attention / Transformer / Embedding / RAG / LoRA
- 构建可部署的 AI 应用，而不是只会调用模型 API
- 具备算法工程师面试所需的 ML / DL / LLM / 数据结构基础
- 在 GitHub 上留下持续可展示的代码与学习记录

## 24 周阶段

| 阶段 | 周数 | 核心目标 |
|---|---:|---|
| 机器学习基础 | 1-4 | sklearn、指标、特征工程、经典模型 |
| 深度学习 / PyTorch | 5-8 | Tensor、Autograd、训练循环、MLP/CNN |
| Transformer / NLP | 9-12 | Embedding、Attention、Transformer、BERT/GPT |
| LLM 工程 | 13-16 | Hugging Face、RAG、Rerank、LoRA、Evaluation |
| 完整项目 | 17-20 | 企业知识库 RAG + API + Docker + 可观测性 |
| 面试冲刺 | 21-24 | ML/DL/LLM、算法题、项目复盘、模拟面试 |

## 今天开始

```bash
cd algorithm-engineer-roadmap
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python week01_ml_basics/train_logistic_regression.py
```

Windows PowerShell 激活命令：

```powershell
.venv\Scripts\Activate.ps1
```

详细安排见 [ROADMAP.md](./ROADMAP.md)，进度打卡见 [PROGRESS.md](./PROGRESS.md)。

## 学习原则

1. 先跑通，再理解，再重写。
2. 每学一个概念，都用代码验证。
3. 每周必须产生 GitHub commit。
4. 数学按需补，不先陷入完整高数教材。
5. 项目必须记录实验结论，而不只是最终代码。
6. 第 17 周开始，把前面的知识整合成一个可部署作品。
