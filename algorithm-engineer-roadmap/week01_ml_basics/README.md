# Week 1 — Machine Learning Basics

## 本周目标

先掌握一个机器学习任务从数据到评估的完整生命周期。

## 必须理解

- 特征 X 和标签 y 是什么？
- 为什么需要 train/test split？
- 为什么 StandardScaler 只能在训练集上 fit？
- Logistic Regression 为什么可以做分类？
- Accuracy 什么时候会骗人？
- Precision 和 Recall 分别适合什么场景？
- F1 为什么是二者的调和平均？
- 什么叫 Data Leakage？
- 什么叫过拟合？

## 实验

运行：

```bash
python train_logistic_regression.py
```

然后至少做 3 个实验：

1. 把 test_size 从 0.2 改成 0.3
2. 修改 LogisticRegression 的 C
3. 移除 StandardScaler，比较结果

把结果记录在本目录新建的 notes.md。

## 思考题

1. 模型训练到底是在“学习”什么？
2. 为什么测试集不能参与训练？
3. 如果 Accuracy=99%，是否说明模型一定很好？
4. Precision 高、Recall 低意味着什么？
5. C 变大后，Logistic Regression 的正则化变强还是变弱？
6. 为什么要用 Pipeline？
7. 如果把 StandardScaler 在完整数据集上 fit，再切训练测试集，会有什么问题？

## 完成标准

你能够不看资料，向别人解释下面这条链路：

```text
Raw Data
  ↓
Train/Test Split
  ↓
Preprocessing
  ↓
Model.fit
  ↓
Model.predict
  ↓
Metrics
  ↓
Error Analysis
```
