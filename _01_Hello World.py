print("Hello Wolrd")
print(100)
print(100+200)
name = "곰돌이 사육사" # 파이썬은 데이터 타입을 선언하지 않아도 됨.
print(name)

name = "정경수"
email = "jks2024@gmail.com"
position = "강사"
address = ("서울시 강남구 역삼동 KH 정보 교육원")

print(f"""
주소 : {address}
직책 : {position}
이름 : {name}
이메일 : {email}
""")

if True :
    print("정상")
else:
    print("오류")

# 작성자 : 정경수
# 목적 : 파이썬 연습용 파일
# 날짜 : 2024.03.18

print(type(38)) # 숫자출력
print(type("문자열 출력"))
print(type([1,2,3]))