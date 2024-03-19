
# 성적에 대한 학점 출력
# 국어, 영어, 수학 성적을 입력 받아 등급 출력
# 평균 90 A , 80 이상 B, 70 이상C 60 이상 D 나머지 F

a,b,c =map(int,input("성적을 입력하세요. :").split())
average = (a+b+c)/3
print(average)
if average >= 90:
    print("A")
elif average >= 80:
    print("B")
elif average >=70:
    print("C")
elif average >=60:
    print("D")
else:
    print("F")
