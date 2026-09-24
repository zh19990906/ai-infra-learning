# Algorithm Engineer — 24 Week Issue Backlog

> GitHub Issues 当前在仓库中处于关闭状态。打开仓库 Settings → General → Features → Issues 后，可将本清单逐条创建为 Issue。

## Phase 1 — Machine Learning

### Week 01 — sklearn 标准训练流程
- [ ] 跑通 Logistic Regression 示例
- [ ] 理解 train/test split 与 stratify
- [ ] 理解 StandardScaler 与 Pipeline
- [ ] 掌握 Accuracy / Precision / Recall / F1
- [ ] 完成 test_size、C、StandardScaler 三组实验
- 交付：week01_ml_basics/notes.md

### Week 02 — Decision Tree / Random Forest
- [ ] 学习 Decision Tree 划分思想
- [ ] 理解 max_depth / min_samples_split
- [ ] 学习 Random Forest 与 Bagging
- [ ] 比较 LR / Decision Tree / Random Forest
- [ ] 分析 feature_importances_
- 交付：模型对比代码与实验结论

### Week 03 — Feature Engineering / Pipeline / CV
- [ ] 缺失值处理
- [ ] 类别特征处理
- [ ] ColumnTransformer / Pipeline
- [ ] Cross Validation
- [ ] Data Leakage
- 交付：完整预处理 Pipeline

### Week 04 — Boosting / Evaluation
- [ ] 理解 GBDT
- [ ] 了解 XGBoost / LightGBM
- [ ] ROC-AUC / PR-AUC
- [ ] 类别不平衡
- [ ] Phase 1 知识复盘
- 交付：第一份 ML 实验报告

## Phase 2 — Deep Learning

### Week 05 — Tensor / Autograd
- [ ] Tensor 基础操作
- [ ] Broadcasting
- [ ] requires_grad
- [ ] backward()
- [ ] PyTorch Linear Regression
- 交付：线性回归训练代码

### Week 06 — PyTorch Training Loop
- [ ] nn.Module
- [ ] Dataset / DataLoader
- [ ] Loss / Optimizer
- [ ] train / eval loop
- [ ] model.train() / model.eval()
- 交付：手写训练循环

### Week 07 — MLP / CNN
- [ ] MLP
- [ ] Activation
- [ ] CNN / Pooling
- [ ] BatchNorm / Dropout
- [ ] 图像分类
- 交付：图像分类项目 + 训练曲线

### Week 08 — Training Tricks
- [ ] Adam / AdamW
- [ ] LR Scheduler
- [ ] Early Stopping
- [ ] Checkpoint
- [ ] 训练日志
- 交付：完善 Week 7 项目

## Phase 3 — Transformer

### Week 09 — Embedding
- [ ] Token / Vocabulary / Embedding
- [ ] Cosine Similarity
- [ ] Sentence Transformers
- [ ] 语义相似度实验
- [ ] 向量检索
- 交付：Embedding 检索 Demo

### Week 10 — Attention
- [ ] Query / Key / Value
- [ ] 手算 Attention
- [ ] Scaled Dot-Product Attention
- [ ] Mask
- [ ] Attention Weights
- 交付：手写 Attention 实现

### Week 11 — Transformer
- [ ] Multi-Head Attention
- [ ] FFN
- [ ] Residual
- [ ] LayerNorm
- [ ] Positional Encoding
- 交付：简化 Transformer Block

### Week 12 — BERT / GPT
- [ ] Encoder-only
- [ ] Decoder-only
- [ ] MLM / Causal LM
- [ ] 文本分类
- [ ] 文本生成
- 交付：分类 Demo + 生成 Demo

## Phase 4 — LLM Engineering

### Week 13 — Hugging Face Ecosystem
- [ ] Transformers
- [ ] Datasets
- [ ] Tokenizer / Model
- [ ] Config
- [ ] Batch Inference
- 交付：Dataset → Tokenize → Inference

### Week 14 — Minimal RAG
- [ ] Chunk
- [ ] Embedding
- [ ] Vector Index
- [ ] Top-K Retrieval
- [ ] Prompt Context
- [ ] Generation
- 交付：最小 RAG Demo

### Week 15 — Reranker / Evaluation
- [ ] Recall@K
- [ ] MRR / NDCG
- [ ] Reranker
- [ ] QA Eval Set
- [ ] Failure Cases
- 交付：RAG 离线评估报告

### Week 16 — LoRA / PEFT
- [ ] SFT
- [ ] LoRA
- [ ] QLoRA
- [ ] PEFT
- [ ] 指令数据格式
- 交付：LoRA 训练实验

## Phase 5 — Portfolio Project

### Week 17 — Document Pipeline
- [ ] 项目需求
- [ ] 文档解析
- [ ] Chunk Strategy
- [ ] Embedding
- [ ] Vector Store
- 交付：Ingestion Pipeline

### Week 18 — Retrieval / Rerank / Generation
- [ ] Retriever
- [ ] Reranker
- [ ] Prompt
- [ ] Citation
- [ ] No-answer Handling
- [ ] Top-K 对比
- 交付：端到端 RAG

### Week 19 — FastAPI / Logging / Tests
- [ ] FastAPI
- [ ] Config
- [ ] Logging
- [ ] Error Handling
- [ ] Unit / Integration Tests
- 交付：可启动 API 服务

### Week 20 — Docker / Benchmark / README
- [ ] Dockerfile
- [ ] 一键启动
- [ ] 架构图
- [ ] Latency / Throughput
- [ ] Quality Metrics
- [ ] README
- 交付：作品级发布版本

## Phase 6 — Interview

### Week 21 — ML Interview
- [ ] Logistic Regression
- [ ] Tree / Random Forest
- [ ] GBDT
- [ ] Regularization
- [ ] Bias / Variance
- [ ] Metrics
- 交付：30 道 ML 面试问答

### Week 22 — DL / LLM Interview
- [ ] Backprop
- [ ] Optimizer
- [ ] Attention / Transformer
- [ ] KV Cache
- [ ] RAG
- [ ] LoRA
- 交付：30 道 DL/LLM 问答

### Week 23 — Data Structures & Algorithms
- [ ] Array / HashMap
- [ ] Stack / Queue
- [ ] Tree / Heap
- [ ] Graph / DFS / BFS
- [ ] Binary Search
- [ ] Dynamic Programming
- 交付：约 100–150 道高质量题 + 模板总结

### Week 24 — Mock Interview / Final Review
- [ ] 3 分钟自我介绍
- [ ] 5 分钟项目介绍
- [ ] 10 个项目追问
- [ ] ML/DL/LLM 模拟问答
- [ ] Coding 模拟
- [ ] 最终薄弱项复盘
- 交付：最终复盘与下一阶段计划
