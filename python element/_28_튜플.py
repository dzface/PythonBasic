
# 값을 변경 할 수 없는 시퀀스 자료형

x = 10
y = "200"
z = 20,
z = 30,
data = 'Alice', 30, "곰돌이 사육사", True # 튜플에 데이터 넣는 것을 Packing이라 지칭
a,b,c,d= data # Unpacking
print(type(x)) # int
print(type(y)) # str
print(z) # 30,
print(type(z)) # tuple
print(a) # person의 변수를 언패킹

# 튜플을 이용한 함수 반환 값 다루기
def get_data():
    name = "곰돌이 사육사"
    age = 25
    addr ="경기도 수원시"
    return name, age, addr

name_card =get_data()
print(name_card)