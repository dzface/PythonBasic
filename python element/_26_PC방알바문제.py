"""
입력 첫째 줄에 손님수 N(N<=100)
둘째 줄에 손님이 들어오는 순서대로 각 손님이 앉고 싶어하는 자리 입력
출력
첫째줄에 거절당하는 사람의 수를 출력
"""


# 미완성
# seat_num = {}
# reject =0
# for i in range(1,101):
#     seat_num[i]=None
# print(seat_num)
#
# while True:
#     N = int(input("손님수 입력: "))
#     seat_num_input = list(map(int,input("자리번호 공백기준 구분하여 입력").split()))
#     for i in range(len(seat_num_input)):
#         if seat_num_input[i] == None :
#             reject = reject +1
#         else:
#             seat_num[i+1] = "사용중"
#     print(reject)
#     print(seat_num_input[1])
#     continue

# 정답
k = list(map(int, input("좌석번호 : ").split()))
pc =[0]*100
cnt = 0
for e in k :
    if pc[e - 1] != 0 : cnt += 1
    else : pc[e - 1] = 1;

print(cnt)