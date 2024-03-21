# 람다(Lambda) : 간단한 함수의 선언과 호출을 하나의 식으로 간략히 표현 한것
# 람다는 주로 이름없는 함수를 만들 때 사용
# 람다의 장점은 일회용 함수가 필요 할 때, 코드의 간견함, 메모리 절약 등이 있음
# 함수와 람다식의 구조비교
# def 함수이름(매개변수):
#      return 결과
# lambda 매개변수 : 결과
def plus(a,b):
    return a+b

print(plus(10,20))
print(lambda a,b: a+b, (10,20))

# 함수의 매개변수로 함수 전달 하기
def call_times(func):
    for i in range(10):
        func()
def print_hello():
    print("Hello!!")

call_times(print_hello)

def power(n): # 입력값의 제곱을 구하는 함수
    return n * n

input_data = map(int, input().split())
rst = list(map(power, input_data))
print(rst)

power2 = lambda  x:x * x  # 입력값의 제곱을 구하는 람다식

input_data = map(int, input().split())
rst = list(map(lambda x:x*x, input_data))
print(rst)