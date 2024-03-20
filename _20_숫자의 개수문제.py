
A, B, C = list(map(int,input("세자리 자연수 3개를 입력하세요. : ").split(" ")))
multiple = str(A * B * C)
# print(multiple)
# print(type(multiple))
for i in range(10) :
    print(multiple.count(str(i)))


