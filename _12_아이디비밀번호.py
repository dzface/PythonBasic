# 회원가입을 위한 아이디/패스워드 입력 확인
user = input("아이디 입력: ")
if len(user) >= 8:
    pwd = input("비밀번호 입력 :")
    if len(pwd) < 8 or len(pwd) > 16:
        print("비밀번호 8자에서 16자 사이여야 합니다.")
    elif pwd.find(user) >=0: #해당문자열의 인덱스를 반환, 없으면 -1
        print("비밀번호에 아이디를  포함 시킬 수 없습니다.")
    else:
        print(f"아이디 : {user}")
        print(f"패스워드 : {pwd}")
else:
    print("아이디는 반드시 8자리 이상이어야 합니다.")
