#
# # 리스트 : 연속적으로 저장되는 형태의 자료형, 크기가 동적으로 변함
# # 자바와 다른점은 여러가지 데이터 타입이 섞여 있을 수 있음, 다중리스트 생성 가능
# # 리스트는 읽기/쓰기 가능, 튜플은 동일한 구조이지만 읽기만 가능
#
# number = [1,2,3,4,5,6,7,8,9]
# fruit = ["appel","banana","orange"]
# mixed = [1,"apple",True,3.14, ["EV6","Santafe","Sorento"]]
#
# print(mixed[4][2][0]) # Sorento의 S 출력 3차원 배열 출력
#
# # 변수와 리스트의 차이 비교
# kor, eng, mat = map(int(input().split())) #변수를 지정할 경우 변수 숫자까지만 입력 가능
# total = kor + eng + mat
# print (total/3)
#
# score = list(map(int, input().split())) # 변수를 유동적으로 입력 가능
# print(sum(score)/len(score))
#
# # 리스트 병합
# list_a = [1,2,3]
# list_b = [4,5,6]
# list_c = list_a + list_b
# print(list_c)
#
# new_list = ["1","2","3"]
# new_list.append(4) # 리스트에 뒤로 값을 추가 java의 add
# new_list.insert(1,1000) # 1번 인덱스에 값 추가
# new_list.pop() # 인덱스가 없으면 마지막 인덱스 값을 반환하고 삭제
# new_list.remove() # 해당 값을 제거 인덱스 x, 동일한 값이 여러개 존재하는 경우 앞에서부터 제거
# new_list.clear() # 내용을 전부 제거하지만 리스트는 제거하지 않음
# # del new_list[3] # 해당 인덱스의 값 제거
#
# # 중복제거
# my_list = ["A","B","C","D","E","A","B"]
# my_list2 = []
# for e in my_list:
#     if e not in my_list2: # 해석 : e가 my_list2에 포함되어 있지 않으면
#         my_list2.append(e)
# print(my_list2)

# 리스트 순회하기
x = ["John", "George", "Paul", "Ringo"]
for e in x:
    print(e)
for i in range(len(x)):
    print(x[i],end="\n")
