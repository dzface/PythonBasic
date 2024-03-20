# 내장 함수? 별도의 import 없이 사용 할 수 있도록 내장도니 함수를 말함

print(max(100, 202, 300))
print(min(100, 202, 300))

print(sum([100, 202,])) # sum() 함수는 튜플이나 리스트 자료형 필요
val = 1,2,3,4,5,6,7,8,9 # 튜플 자료형
print(f"평균 : {sum(val)/len(val)}")
# 몫과 나머지
print(divmod(sum(val),4)) # 목과 나머지 튜플만 가능

# 외장 함수 : 파이썬의 표준 모듈이지만 import 해야 사용 가능
import random
rand =random.randint(0,4) # 0~4사이의 임의의 정수 반환 4를 포함
for i in range(10):
    rand = random.randint(0, 4)  # 0~4사이의 임의의 정수 반환 4를 포함
    print(rand)
    rand2 = random.randrange(0,4) # 0~4 미만
    print(rand2)

# 날짜 및 시간 관련 처리 모듈
from datetime import datetime # datetime 모듈에서 datetime 함수만 import
datetime.today() # 현재 날짜 가져오기
print(datetime.today().year)# 현재연도 가져오기
print(datetime.today().month)
print(datetime.today().day)
print(datetime.today().hour)
print(datetime.today().minute)
print(datetime.today().second)

import calendar

print(calendar.calendar(2024))
print(calendar.calendar(2024,m=5))
print(calendar.month(2024,3))

import math

print(math.sin(2))
print(math.ceil(1.00000001)) # 소숫점 올림
print(math.floor(1.9999999)) # 소숫점 내림