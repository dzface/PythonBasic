# 결정트리는 분류나 회귀 문제를 해결하기 위해 사용되는 지도학습 알고리즘

#루트 노드 :트리아 최상위, 전체 데이터 집합을 대표
#내부 노드 : 특성에 대한 검사를 수행하고 데이터를 두개이상의 하위 그룹으로 분할
#리프노드 : 더 이상의 분할이 일어나지 않는 최종노드, 분류 결정이나 회귀 값을 가짐

# 필요한 라이브러리 임포트
import pandas as pd
import numpy as np
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn import tree
import matplotlib.pyplot as plt

# 가상 데이터 생성
X, y = make_classification(n_samples=1000, n_features=10, n_informative=5, n_classes=2, random_state=42)
# 특징 이름 생성
feature_names = [f'feature_{i}' for i in range(X.shape[1])]

# 데이터프레임으로 변환
df = pd.DataFrame(X, columns=feature_names)
df['target'] = y

# 데이터 분할
X_train, X_test, y_train, y_test = train_test_split(df[feature_names], df['target'], test_size=0.3, random_state=42)

# 결정트리 모델 생성 및 학습
clf = DecisionTreeClassifier(random_state=42)
clf.fit(X_train, y_train)

# 테스트 데이터로 예측 : 학습된 모델을 사용하여 테스트 데이터에 대한 예측을 수행
y_pred = clf.predict(X_test)

# 정확도 평가 : 예측 결과와 실제 값을 비교하여 모델의 정확도를 계산하고 출력
accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy:.2f}')

# 결정트리 시각화
plt.figure(figsize=(16,10))
tree.plot_tree(clf, filled=True, feature_names=feature_names, class_names=['No Default', 'Default'])
plt.show()