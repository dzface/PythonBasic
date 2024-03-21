
# 1~45까지번호 6개 자동 생성
from random import *
lotto=[]
for i in range(6):
 rand = int(randrange(1,46))
 if rand not in lotto:
     lotto.append(rand)
 if len(lotto) == 6:
     break

# 임의의 수를 연속(공백)으로 입력 받아 홀수, 짝수 리스트로 나누어 담기
# 입력 1 2 3 4 5 6 7 8 9 10
# 출력
# 홀수 : 1 3 5 7 9
# 짝수 : 2 4 6 8 10

list = list(map(int, input("숫자를 공백기준으로 입력: ").split()))

list_odd = []
list_even= []
for i in range(len(list)):
    print(list[i])
    if list[i]%2 != 0:
        list_odd.append(list[i])
    else:
        list_even.append(list[i])
print(f"홀수 : {list_odd}\n짝수 : {list_even}")

# 방법 2
for e in list:
    if e % 2 ==0: list_odd.append(e)
    else: list_odd.append(e)
print(f"홀수 : {list_odd}\n짝수 : {list_even}")

# 방법 3
list = list(map(int, input("정수 입력 :").split()))
even = list(filter(lambda x:x %2==0, list))
odd = list(filter(lambda x:x %2 ==1,list))
print(f"홀수 : {odd}\n짝수 : {even}")
