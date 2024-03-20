#
# name = input("이름 입력 :")
#
# age = int(input("나이 입력 :"))
# while 0 > age or age >200:
#     age = int(input("나이를 다시 입력하세요 : "))
#
# gender = input("성별을 입력하세요. M/F: ")
# while gender != "M" or gender != "m" or gender != "F" or gender != "f":
#     if gender == "M" or gender == "m":
#         break
#     elif gender == "F" or gender == "f":
#         break
#     else:
#         gender = input("성별을 다시 입력하세요. M/F: ")
#
# if gender == "M" or gender == "m":
#     gender = "남자"
# elif gender == "F" or gender == "f":
#     gender = "여자"
#
# job = int(input("직업을 입력 :[1]학생 [2]회사원 [3]주부 [4]무직"))
# while type(job) != type(1):
#     job = int(input("직업을 다시 입력하세요. :\n [1]학생\n[2]회사원\n[3]주부\n[4]무직"))
#
# print(f"이름: {name}\n나이: {age}\n성별: {gender}\n직업: {job}")

#### 함수형 프로그래밍 ####

def input_age():
    while True:
        age = input("나이를 입력 :")
        if age.isdigit(): # 문자열이 숫자로 구성되어 있는지 확인
            age = int(age)
            if 0 < age < 200:
                return age
        print("나이를 잘 못 입력 했습니다.")

def input_gender():
    while True:
        gender = input("성별 입력 : ")
        if gender =="M" or gender == "m": return "남성"
        elif gender =="F" or gender == "f": return "여성"
        print("성별을 잘 못 입력 했습니다.")

def input_jobs():
    while True:
        jobs = input("직업 입력 : ")
        if jobs.isdigit():
            jobs = int(jobs)
            if 0<jobs<5: return jobs
        print("직업을 잘못 입력하셨습니다.")

def print_info(name,age,gender,jobs):
    jobs_str = "", "학생", "회사원", "주부", "무직" # 괄호 없이 생성하면 튜플생성
    print("="*3, "회원정보", "="*3)
    return f"이름 : {name}\나이 : {age}\n성별 : {gender}\n직업 : {input_jobs()}"

# 함수 호출하고 파일 저장하기
fd = open("member.txt", "wt", encoding="utf-8")
while True:
    name = input("이름 입력 / 종료는 quit :")
    if name == "quit": break
    age = input_age()
    gender = input_gender()
    jobs = input_jobs()
    rst = print_info(name,age,gender,jobs)
    fd.write(rst + "\n")
fd.close()
