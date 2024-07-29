

# 호출 방법 1
# import _43_모듈과패키지 as mod
# print(mod.add(100,200))
# print(mod.sub(200,200))
# print(mod.password("http://naver.com"))

# 호출 방법 2
from _43_모듈과패키지 import add, sub, password
print(add(100,200))
print(sub(200,200))
print(password("http://naver.com"))