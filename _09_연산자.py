
# 연산자란? 프로그램에 계산을 위해서 사용 (사칙, 대입, 비교, 관계, 비트 연산 등이 있음)
# 산술연산 : +, -, *, /(나누기), %(나머지), //(몫), **(제곱 연산자) 증감연산자는 없음
i = 10
j = 3

print(i+j)
print(i**j) # 10의 3제곱
print(i/j) # 나# 누기
print(i//j) #몫 몫 연산자가 있는 이유?
print(f"{i/j:2f}") # 나누기
text = "Python"
print(text *3)

tax_rate = 0.10
income = int(200000)
print(f"당신이 내야 할 세금은 {income * tax_rate:.2f} 입니다.")

# 관계(논리)연산자
x= 10
y= 20
z= 30
rst1 = x > 0 and x > y # &&, 둘다 참이어야 참
rst2 = x > 0 or x > y # ||, 둘중 하나만 참이여도 참
rst3 = not(x > 0 or x > y) # !, 참이면 거짓, 거짓이면 참으로 변환
print(rst1, rst2, rst3)

# 3항 연산자    자바는 ? 참: 거짓,
age = int(29)
adult = age >18 and "성인" or "미성년자" # 파이썬 (조건식) and 참인경우 수행 or 거짓인 경우 수행
print(f"당신은 {adult} 입니다.")

num = int(20)
is_even = num % 2 == 0 and "짝수" or "홀수"
print(is_even)

# 진법 표기
print(bin(42)) # 2진법 b (binary)
print(42 == 0b101010)
print((oct(42)))# o 8진법 (octa)
print(42 == 0o52)
print(hex(42)) # x 16진법 (hexa)
print(42 == 0x2a)

# 비트 연산자 2진법
a = 10
b = 12
print( a & b) # 둘다 1이어야 1
print( a | b) # 둘 중 하나만 1이면 1
print(a ^ b) # 값이 다른 경우 1, 6
print(~a) # 비트 반전, 음수 표기는 2의 보수로 표기 하기 때문에 1이 모자람
print(a << 1) # 주어진 값 만큼 왼쪽으로 이동
print(a >> 1) #