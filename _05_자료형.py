# 파이썬은 변수 선언 시 데이터 타입을 지정하지 않으며
# 변수에 값이 대입 될 때 자료형이 결정 됨.

number = 200
number2 = 3.14
text = ""
suppose = True
print(type(number)) # type() : 변수의 자료형 확인
print(type(number2))
print(type(str))
print(type(bool))

# 형변환: 선언된 변수의 자료형을 다른 자료형으로 변경 할 때 사용
print(10 + int("10"))
print("나이 :" + str(30))
print(0.1*float("512.34"))
var = "" # 공백은 거짓
false1 = 0 # 0 은 거짓
false2 = None
print(bool(number)) # boolean 값의 거짓 : "", 0, False, None 나머지는 다 참


