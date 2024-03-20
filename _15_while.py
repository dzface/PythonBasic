# whiel문 : 참인 동안 반복 수행, 반복횟수를 알 수 없을 때 주로 사용

# 입력 받은 정수의 합 구하기
n = int(input("정수 입력 : "))
sum = 0
while n : # 자바에서는 boolean 조건문만 가능
    sum += n
    n -= 1 # n-- 파이썬에서는 증감코드가 없어서 안됨
print(sum)

while True:
    age = int(input("나이를 입력 :"))
    if 0 <= age <200: break
    print("나이 입력 범위를 벗어 났습니다.")