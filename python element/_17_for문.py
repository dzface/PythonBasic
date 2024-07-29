#
# # for문은 정해진 범위 만큼 반복 할 때 주로 사용
# # for 요소 in 시퀀스 : 시퀀스는 리스트, 튜플, 문자열, 등을 의미
# # 자바의 향상된 for와 유사
#
#
# # for 순회
# fruits = ["사과","바나나","딸기","수박","참외","복숭아"]
# for e in fruits:
#     print(e,end="_")
# print("\n")
#
# # for 변수 in range (시작값, 종료값, 증감값) : 자바의 기본 for문과 유사
# n = int(input("정수 입력 : "))
# sum = 0
# for i in range(1, n+1): # 1부터 n+1 미만 까지 순회 증감값은 생략하면 1씩 증가
#     sum+=i
# print(sum)

# # 이중 for문 사용하기 10x10 정사각형 생성
# n = int(input("정수를 입력 :"))
# for i in range(n):
#     for j in range(n):
#         print("*",end=" ")
#     print()

# # 구구단 출력
# for i in range(2,10):
#     for j in range(1,10):
#         print(f"{i} x {j} = {i*j}")
#     print("----------")

# # 이중for문과 조건문 사용
# n = int(input("정수를 입력하세요. : "))
# for i in range(0,n):
#     for j in range(0,n):
#         if j % 2 ==0: #짝수이면
#             print("#", end=" ")
#         else:
#             print("*", end=" ")
#     print()

# # 사각형 찍기 실습
# n = int(input("정수 입력 : "))
# for i in range(0,n):
#     for j in range(0,n):
#          print("*", end=" ")
#     print()

# 행렬 출력 실습
# n = int(input("정수를 입력 하세요 : "))
# for i in range(1, n * n + 1):
#     print(f"{i:3}", end='')    #이쁘게 찍기 위해서 오른쪽 정렬 한다. 왼쪽 정렬은 <
#     if i % n == 0: print()

# # 우측정렬 삼각형
# n = int(input("정수 입력 : "))
# for i in range(0,n+1):
#     for j in range(0,i):
#          print("*", end=" ")
#     print()

# # 우측정렬 역삼각형
# n = int(input("정수 입력 : "))
# for i in range(n,0,-1):
#     for j in range(i,0,-1):
#          print("*", end=" ")
#     print()
# 방법 2
# n = int(input("정수 입력 : "))
# for i in range(n):
#     for j in range(n-i):
#          print("*", end=" ")
#     print()

## 좌측정렬 역삼각형
# n = int(input("정수 입력 : "))
# for i in range(n):
#     for k in range(i):
#         print(" ", end="")
#     for j in range(n-i):
#         print("*" ,end="")
#     print()

# # for문에서 continue 사용
# n = int(input("정수 입력 :"))
# for i in range(n):
#     if i%2 ==0 :continue # 짝수이면 아래 코드는 수행안하고 다시 반복문 실행
#     print(i, end=" ")
#
# # for 문 반대로 반복하기
# for i in range(10, 0-1, -1): # 10에서 -1 미만까지 순회
#     print(f"index : {i}")

# for문으로 알파벳 출력하기:
# # chr(유니코드값을 입력 받아 문자 출력)
# # ord(문자의 유니코드 값을 반환)
#
# for i in range(ord("A"),ord("Z")+1):
#     print(chr(i), end=" ")
# print()
#
# for i in range(65,91) : # A:65, Z:90
#     print(chr(i),end=" ")