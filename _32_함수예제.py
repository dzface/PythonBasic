
#순차 검색 함수
def search_list(a,x):
    for i in range(len(a)):
        if x ==a[i]: return i
    return  -1

v = [17,92,18,33,58,7,33,42]
print(search_list(v,33))
print(search_list(v,18))
print(search_list(v,30)) # v 에 없으므로 -1

# 기본값 인자
# 기본값 인자 : 파이썬은 매개 변수에 대한 기본값을 정의 할 수 있음
# 함수 호출 시 인자값을 넣지 않으면 매개 변수의 기본값이 반영 됨
def profile(name, year =2, age =18, school = "태양고"): # 함수사용시 값이 없는 매개변수는 필수로 입력해야함
    print(f"이름 : {name}, 학교 : {school}, 학년 : {year}, 나이 : {age}")

profile("나희도")
profile("고유림")
profile("백이진", None,22)

# 가변 매개변수: 함수의 매개변수 앞에 *을 붙여주면 함수의 매개변수를 몇개를 입력하든 상관없음
def profile2(name,age,*lang):
    print(f"이름 : {name}, 나이 : {age}", end=" ")
    for e in lang:
        print(e, end= " ")
    print()

profile2("나희도",18, "Python","Java", "C", "C++","React","Kotlin")
profile2("조세호", 38, "Pythob", "Java")
profile2("유재석", 48, "C","C++")