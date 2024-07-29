
# 3개의 정수를 입력 받아 최대값/최소값 구하기
a, b, c = map(int, input("숫자 3개를 스페이스바로 구분하여 입력하세요. : ").split())
list = [a,b,c]

print("최대값 :" + str(max(list)) + "\t최소값 :" +str(min(list)))



# 주민등록번호를 입력받아 생년월일, 성별, 나이 출력하기
jumin = input("주민등록번호 13자리를 입력하세요")
gender = jumin[6]
if jumin[6] == "1" or jumin[6] == "3":
    gen = "남자"
elif jumin[6] == "2" or jumin[6] == "4":
    gen = "여자"
else:
    print("성별오류")

print(
"생년월일 :" + str(jumin[:6]) + "\n" +
"성별 : " + str(gen) +"\n"
"나이 : " + str( 2024 - 1900 - int(jumin[:2]))
)

# 2개의 문자열을 변수 s와 k에, 양의 정수를 변수 n에 각각 전달 받아
# s 문자열의 두 부분의 n개 문자를 k문자열 앞에 끼워 넣는 코드 작성
# 예) s:seoul K:korea n: 2 result : ulkorea

s, k = map(str, input("스페이스바로 구분하여 영어 단어 두개를 입력하세요. : ").split())
n = int(input("정수1개를 입력하세요. : "))
result = str(s[-n:]) + k
print(result)

#여러개의 정수를 입력 받아 합계와 평균 구하기
num2 = list(map(int, input("정수 여러개").split()))
print(f"합계 : {sum(num2)}")
print(f"평균 : {sum(num2)/len(num2)}")