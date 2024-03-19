# 문자열 : 문자로 이루어진 데이터 집합, 파이썬은 문자를 별도로 다루지 않고 전부 문자열로 간주
# "", '', """ """, ''' '''

# 인덱싱이란 : 시퀸스 자료형(리스트, 튜플, 문자열) 특정 문자열에서 특정 위치 요소를 선택하는 작업
# seq[index]
# 슬라이싱이란 : 시퀀스 자료형에서 일부분을 추출
# seq[start:end:step]

my_list = [0,1,2,3,4,5,6,7,8,9]
slice_without_step = my_list[2:7] # 인덱스는 0부터 시작, 미만
slice_with_step = my_list[1:9:2]

# 인덱싱, 슬라이싱 실습
# 주민등록번호 자르기, 하위 7자리 중 첫번째 글자는 성별, 앞의 6자리는 년,월,일

jumin = "991120-1234567"
print("성별 :" + jumin[7])
print("년 : "+ jumin[:2])
print("월 : "+jumin[2:4])
print("일 : "+jumin[4:6])
print("생년월일 :"+jumin[:6])
print("뒤 7자리 :"+ jumin[7:])
print("뒤 7자리 :"+ jumin[-7:])

python_str = "Life is too short, You need Python"
new_str = python_str[0] + python_str[1]+python_str[2]+python_str[3]
# python_str[0]= "l" # str은 리터럴 상수이기 때문에 요소 하나만 변경 안됨

print(python_str.upper()) # 모두 대문자로 출력
print(python_str.lower())

a_str = "Hello Python Program"
print(a_str.replace("Python","JavaScript")) # 원본은 바뀌지 않음
new_str2 = a_str.replace("Python","JavaScript")

# 문자열에 포함된 문자 갯수 세기 count(), 문자열 길이 (len(), __len__())
print(a_str.count("l")) # 해당 문자열에서 count() 함수에 전달문자가 몇개 존재하는지 반환
print(len(a_str)) # 문자열 길이를 반환하는 함수
print(a_str.__len__()) # 문자열 길이를 반환하는 내장 함수

# 문자열 찾기
# find() : 찾은 문자열 반환 없으면 -1
# rfind() : 뒤에서 문서 문자열 찾고 찾은 인덱스는 앞에서 계산 
# index() : 찾은 문자열의 인덱스 반환, 없으면 ValueError
phrase = "가장 큰 실수는 포기, 가장 어리석은 일은 남의 결점 찾기, 가장 좋은 선물은 용서"
print(phrase.find("가장"))
print(phrase.rfind("가장"))
print(phrase.index("가장"))
input_a = '''
안녕하세요.
문자열 함수를 알아 봅시다.
'''
print(input_a.strip()) # 문자열 처음과 끝의 공백제거
