# 세자리수 중에서 가장 큰 수 153
number = int(input("세자리 정수를 입력하세요. :"))
str_number= str(number)
list = {str_number[0],str_number[1],str_number[2]}
print(max(list))

# sol2
n = int(input("정수 입력 : "))
a = n // 100 # 100으로 나눈 몫을 구함
b = (n % 100) //10 # 100으로 나눈 나머지에서 다시 10으로 나눈 몫 구하기
c = n % 10 # 10으로 나눈 나머지
if a > b:
    if a > c: print(a)
    else: print(c)
else:
    if b > c: print(b)
    else: print(c)
    
# 주/야간 근무시간을 입력받아 아르바이트 급여 계산하기
# 시급: 9620원 야근: 시급 *1.5

work = input("주간근무[1]. 야간근무[2] 중 선택하세요. : ")
time = int(input("근무 시간을 입력해 주세요. :"))
pay = int(9620)
total = pay * time
if work == "1":
    print(f"입력한 시간 동안 근무한 주간 또는 야간 급여는 {total}원 입니다.")
elif work == "2":
    print(f"입력한 시간 동안 근무한 주간 또는 야간 급여는 {int(total*1.5)}원 입니다.")