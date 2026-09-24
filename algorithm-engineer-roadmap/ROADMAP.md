# 24 周算法工程师学习路线

## Phase 1：机器学习基础（Week 1-4）

### Week 1 — sklearn 标准训练流程
学习：train/validation/test、标准化、Logistic Regression、Accuracy、Precision、Recall、F1、混淆矩阵。

交付物：
- 跑通 Logistic Regression 示例
- 修改 test_size / random_state / C，比较结果
- 写一份实验记录

### Week 2 — 树模型
学习：Decision Tree、Random Forest、过拟合、特征重要性。

交付物：同一数据集比较 Logistic Regression / Decision Tree / Random Forest。

### Week 3 — 特征工程与数据泄漏
学习：缺失值、类别特征、标准化、Pipeline、交叉验证、Data Leakage。

交付物：完成一个包含预处理 Pipeline 的表格数据项目。

### Week 4 — Boosting 与模型评估
学习：GBDT、XGBoost/LightGBM 思想、ROC-AUC、PR-AUC、类别不平衡。

交付物：完成第一份完整 ML 实验报告。

---

## Phase 2：PyTorch 与深度学习（Week 5-8）

### Week 5 — Tensor / Autograd
手写 Tensor 运算、梯度计算、Linear Regression。

### Week 6 — 神经网络训练循环
掌握 nn.Module、Dataset、DataLoader、Loss、Optimizer。

交付物：不依赖 Trainer，手写完整训练循环。

### Week 7 — MLP / CNN
理解激活函数、BatchNorm、Dropout、卷积。

交付物：完成图像分类任务。

### Week 8 — 训练技巧
学习 Adam/AdamW、Learning Rate、Scheduler、Early Stopping、Checkpoint。

交付物：给 Week 7 项目增加训练日志和模型保存。

---

## Phase 3：Transformer / NLP（Week 9-12）

### Week 9 — Embedding
理解 token、词向量、相似度、向量检索。

### Week 10 — Attention
手算并代码实现 Scaled Dot-Product Attention。

### Week 11 — Transformer
理解 Multi-Head Attention、FFN、Residual、LayerNorm、Position Encoding。

交付物：自己实现一个简化 Transformer Block。

### Week 12 — BERT / GPT
理解 Encoder-only、Decoder-only、预训练与生成。

交付物：用 Hugging Face 跑通一个文本分类和一个生成任务。

---

## Phase 4：LLM 工程（Week 13-16）

### Week 13 — Hugging Face 生态
Transformers、Datasets、Tokenizer、模型加载、推理。

### Week 14 — RAG
Chunk、Embedding、Vector Search、Top-K、上下文拼接。

交付物：实现一个最小 RAG。

### Week 15 — Reranker 与 Evaluation
理解 Recall、MRR、NDCG、RAG evaluation、幻觉问题。

交付物：给 RAG 增加离线评估集。

### Week 16 — LoRA / PEFT
理解 SFT、LoRA、QLoRA、训练数据格式。

交付物：完成一个小模型 LoRA 实验或完整训练脚本。

---

## Phase 5：作品级项目（Week 17-20）

项目：Enterprise Knowledge Base RAG

```text
Documents
   ↓
Parser / Chunker
   ↓
Embedding
   ↓
Vector Store
   ↓
Retriever
   ↓
Reranker
   ↓
LLM
   ↓
FastAPI
   ↓
Evaluation / Logging
```

### Week 17
文档解析、Chunk、Embedding、向量检索。

### Week 18
Retriever、Reranker、Prompt、引用来源。

### Week 19
FastAPI、配置管理、日志、错误处理、测试。

### Week 20
Docker、README、架构图、Benchmark、项目复盘。

最终项目至少回答：
- 为什么这样切 Chunk？
- 为什么选择这个 Embedding？
- Top-K 如何选择？
- Reranker 带来了多少提升？
- 延迟瓶颈在哪里？
- 如何评估回答质量？

---

## Phase 6：面试与查漏补缺（Week 21-24）

### Week 21 — 机器学习面试
LR、Tree、Random Forest、GBDT、过拟合、正则化、Bias/Variance、指标。

### Week 22 — 深度学习 / LLM 面试
Backprop、Optimizer、Attention、Transformer、KV Cache、RAG、LoRA。

### Week 23 — 数据结构与算法
重点：Array、HashMap、Stack/Queue、Tree、Heap、Graph、DFS/BFS、Binary Search、DP。

目标不是刷数量，而是形成模板；累计完成约 100～150 道高质量题。

### Week 24 — 项目复盘与模拟面试
准备：
- 3 分钟自我介绍
- 5 分钟项目介绍
- 10 个项目追问题
- 机器学习基础题
- Transformer/LLM 基础题
- 现场 Coding

## 每周固定复盘模板

1. 本周学了什么？
2. 哪 3 个概念还解释不清？
3. 写了什么代码？
4. 做了什么实验？
5. 哪个结果和预期不同？
6. 下周需要补什么？
