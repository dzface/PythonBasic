
# 집합자료형은 주로 중복제거용 사용
# 순서를 보장하지 않음
# 중복 불가
# mutable(Read / Write) 가능

s1 = set([1,2,3,4,5,6])
s2 = set([4,5,6,7,8,9])
s3 = s1.union(s2) # 합집합, 중복제거
s4 = s1.intersection(s2) # 교집합
s5 = s1.difference(s2) # 차집합


# 집합 중복제거를 이용한 로또 번호 추출
import random
lotto_num = set()
while True:
    num = random.randrange(1,46)
    lotto_num.add(num)
    if len(lotto_num) == 6:break
print(lotto_num)