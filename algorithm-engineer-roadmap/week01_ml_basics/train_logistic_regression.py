"""Week 1: 一个完整、可复现的 sklearn 二分类训练示例。"""

from sklearn.datasets import load_breast_cancer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix,
    f1_score,
    precision_score,
    recall_score,
)
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler


RANDOM_STATE = 42


def main() -> None:
    dataset = load_breast_cancer()
    X, y = dataset.data, dataset.target

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=RANDOM_STATE,
        stratify=y,
    )

    model = Pipeline(
        steps=[
            ("scaler", StandardScaler()),
            (
                "classifier",
                LogisticRegression(
                    C=1.0,
                    max_iter=2000,
                    random_state=RANDOM_STATE,
                ),
            ),
        ]
    )

    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    print(f"train samples: {len(X_train)}")
    print(f"test samples : {len(X_test)}")
    print()
    print(f"accuracy : {accuracy_score(y_test, y_pred):.4f}")
    print(f"precision: {precision_score(y_test, y_pred):.4f}")
    print(f"recall   : {recall_score(y_test, y_pred):.4f}")
    print(f"f1       : {f1_score(y_test, y_pred):.4f}")
    print()
    print("confusion matrix:")
    print(confusion_matrix(y_test, y_pred))
    print()
    print("classification report:")
    print(
        classification_report(
            y_test,
            y_pred,
            target_names=dataset.target_names,
        )
    )


if __name__ == "__main__":
    main()
