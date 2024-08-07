import pandas as pd

# 데이터 로드
df = pd.read_csv('https://raw.githubusercontent.com/pandas-dev/pandas/main/doc/data/titanic.csv')

# 데이터 정보 출력
print(df.info())
print(df.head())
print(df.describe())

# 데이터 전처리
# 결측치 확인
print(df.isnull().sum())

# 결측치 처리: Age의 결측치를 평균값으로 대체
df['Age'].fillna(df['Age'].mean(), inplace=True)

# Embarked의 결측치를 최빈값으로 대체
df['Embarked'].fillna(df['Embarked'].mode()[0], inplace=True)

# 새로운 열 추가: 가족 수(FamilySize)
df['FamilySize'] = df['SibSp'] + df['Parch'] + 1
print(df.head())

# 데이터 분석
# 생존자 비율
survival_rate = df['Survived'].mean()
print(f"Overall Survival Rate: {survival_rate * 100:.2f}%")

# 성별에 따른 생존자 비율
survival_rate_by_gender = df.groupby('Sex')['Survived'].mean()
print(survival_rate_by_gender)

# 클래스에 따른 생존자 비율
survival_rate_by_class = df.groupby('Pclass')['Survived'].mean()
print(survival_rate_by_class)

# 데이터 시각화
import matplotlib.pyplot as plt
import seaborn as sns

# 성별에 따른 생존자 비율 시각화
sns.barplot(x='Sex', y='Survived', data=df)
plt.title('Survival Rate by Gender')
plt.show()

# 클래스에 따른 생존자 비율 시각화
sns.barplot(x='Pclass', y='Survived', data=df)
plt.title('Survival Rate by Class')
plt.show()

# 나이에 따른 생존자 비율 시각화
plt.figure(figsize=(10, 6))
sns.histplot(df[df['Survived'] == 1]['Age'], bins=30, label='Survived', kde=False, color='green')
sns.histplot(df[df['Survived'] == 0]['Age'], bins=30, label='Not Survived', kde=False, color='red')
plt.legend()
plt.title('Survival Rate by Age')
plt.show()

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
from sklearn.preprocessing import StandardScaler

# 필요한 열 선택 및 더미 변수화
df = pd.get_dummies(df, columns=['Sex', 'Embarked'], drop_first=True)

# 특성과 타겟 변수 정의
X = df[['Pclass', 'Age', 'SibSp', 'Parch', 'Fare', 'FamilySize', 'Sex_male', 'Embarked_Q', 'Embarked_S']]
y = df['Survived']

# 데이터 스케일링
scaler = StandardScaler()
X = scaler.fit_transform(X)

# 훈련 세트와 테스트 세트로 분리
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 로지스틱 회귀 모델 훈련
model = LogisticRegression(max_iter=500)
model.fit(X_train, y_train)

# 예측
y_pred = model.predict(X_test)

# 정확도와 분류 보고서 출력
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy * 100:.2f}%")
print(classification_report(y_test, y_pred))
