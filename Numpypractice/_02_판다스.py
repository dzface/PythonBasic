import pandas as pd
import numpy as np

s1 = pd.Series([10, 20, 30, 40, 50]) # 리스트 구조로 데이터를 입력
print(s1) # 출력 결과에 인덱스가 포함되어서 출력이 됨

s2 = pd.Series(['a', 'b', 'c', 1, 2, 3])
print(s2)

# 데이터가 없는 경우에 대한 처리
s3 = pd.Series([np.nan, 10, 20, 30])
print(s3)

# 인덱스 추가하기
index_date = ['2024-07-26', '2024-07-27', '2024-07-28', '2024-07-29']
s4 = pd.Series([200, 300, np.nan, 500], index_date)
print(s4)

# 딕셔너리로 인덱스 추가하기
s5 = pd.Series({'국어':100, '영어':95, '수학':85})
print(s5)

# 날짜 자동생성
s6 = pd.date_range(start='2024-07-20', end='2024-07-28')
print(s6)
# 달력을 요일을 기준으로 일주일씩 증가
s7 = pd.date_range(start='2024-07-20', periods=4, freq='W')
print(s7)

# 데이터프레임은 행과 열로 구성된 사각형 모양의 표
df = pd.DataFrame({
    'name' : ['민지', '하니', '혜린', '다니엘', '혜인'],
    'kor' : [90, 88, 97, 77, 60],
    'eng' : [88, 99, 70, 100, 80]
})
print(df)
print(df['eng'])

print(sum(df['eng'])/df['eng'].size)
