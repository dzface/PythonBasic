# # 함수로 짝수 홀수 판단
#
# def even_odd_checker (n):
#     if n % 2 == 0:
#         print("짝수")
#     else:
#         print("홀수")
#
# x = even_odd_checker(0)
#
# # 입력으로 들어오는 수 평균 구해서 반환후 출력
# def average(input_number):
#     return sum(input_number)/ len(input_number)
#
# x=list(map(int, input("정수 입력 :").split(" ")))
# print(average(x))

# 입력 숫자 이하의 소수들의 합 함수 미완
def prime(input_number):
    x = int(input("정수 입력 :"))
    prime_sum = 0
    for i in range(2, x):
        if type(x / i) != type(3.14): # 소수 : 나눌 수 있는 수가 자기자신과 1일 때
            prime_sum += i
    print(prime_sum)







