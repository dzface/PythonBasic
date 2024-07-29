import pandas as pd

df = pd.DataFrame({
    '제품' : ['사과', '딸기', '수박'],
    '가격' : [1800, 1500, 3000 ],
    '판매량' : [24, 38, 13]
})
print(df)

print(f" 평균가격 : {sum(df['가격'] / df['가격'].size)}")
print(f" 평균판매량: {sum(df['판매량'] / df['판매량'].size)}")
