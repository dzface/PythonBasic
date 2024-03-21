
# 이미 만들어져 있는 함수의 앞고 뒤에 기능을 추가 할 때 사용됨
# 스프링부트에서는 AOP(Aspect, Oriented Progrmming)이라고 부름

from datetime import datetime

def datetime_deco(func):
    def decorated():
        print(datetime.now())
        func()
        print(datetime.now())
    return decorated

@datetime_deco
def for_sum():
    sum=0
    for i in range(1,100):
        sum += i
        print(sum)

for_sum()