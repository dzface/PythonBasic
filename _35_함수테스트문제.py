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

# 입력 숫자 이하의 소수들의 합 함수 미완료

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    max_divisor = int(n ** 0.5) + 1
    for i in range(3, max_divisor, 2):
        if n % i == 0:
            return False
    return True

def sum_of_primes(N):
    prime_sum = 0
    for num in range(2, N + 1):
        if is_prime(num):
            prime_sum += num
    return prime_sum

N = int(input("정수 입력: "))
result = sum_of_primes(N)
print(f"{N} 이하의 소수를 모두 더한 결과 값은 {result} 입니다.")







