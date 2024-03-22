# 모듈 : Phython의 코드를 포함하는 파일(.py)
# 모듈에는 함수, 클래스, 변수 등을 포함 할 수 있으며,
# 이러한 요소들은 다른 python 파일에서 import해서 사용 할 수 있음

# 패키지 : 모듈의 집합, 즉 여러개의 모듈을 포함하는 디렉토리를 의미

# import math # 모듈 내의 함수를 사용하기 위해 모듈을 불러 올때
# print(math.cos(2))
# print(math.pow(2,10))

# from math import sin, cos, pow # 모듈 내의 일부 함수만 불러올 때
# print(sin(1))
# print(pow(2,10))

# from pandas import * # pandas 모듈 전체 불러 올때
# import pandas as pd  # 약어 사용 할 때



def add(a,b):
    return a +b
def sub(a,b):
    return a -b
def password(url):
    my_str = url.replace("http://", "")
    my_str = my_str[:my_str.index(".")] # 슬라이싱, 처음부터 . 위치 미만까지
    password = my_str[:3] + str(len(my_str)) + str(my_str.count("o")) + str(my_str.count("o")) + "!" + "Jks" + "2024"
    return password

if __name__ == "__main__": # 해석 함수에 대한 사용 파일이 동일한지? 동일하면 함수 사용해라
    print(add(1,4))  # 다른 파일에서 __name__ == "__main__" 써도 함수 적용 x
    print(sub(4,2))

