# 조건문과 반복문은 제어문이라하고, 이는 수차적인 흐름을 제어하는 목적으로 사용
# 2 파이썬의 조건문 자바의 if 문과 switch문을 결합한 형태와 유사하며, 파이썬은 switch문 없음
# 조건문의 수행은 들여쓰기를 구분하고 각각의 조건은 :(클론)으로 구분

num = int(input("정수를 입력 하세요 :"))

if num > 0:
    print("양수입니다. ")

elif num < 100:
    print("음수 입니다.")
else:
    print("입력값이 100과 같아요")


season = input("지금 계절은")
if season == "spring" :
    print("따듯한 봄 입니다.")
elif season == "summer" :
    print("무더운 여름입니다.")
elif season == "fall" or season == "autumn":
    print("쓸쓸한 가을 입니다.")
else:
    print("추운 겨울 입니다.")

