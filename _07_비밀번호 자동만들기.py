"""
### 응용 예제 2번

***각 사이트 비밀번호 자동으로 만들기***

규칙1 : http://naver.com에서 앞의 http:// 잘라내기

규칙2 : 처음 만나는 점(.) 이후는 제외

규칙3 :
남은 글자 중 처음 세자리 +
글자 갯수 +
글자에 포함된 'o' 갯수 +
글자에 포함된 'k' 갯수+
'!' +
자신의이니셜(예: 'jks')

"""
file_name = "pwd.txt"
f= open(file_name, "wt")
while True:
    url = input("사이트 :")
    if url == "exit": break
    my_str = url[5:] # 처음 문자열 제거
    print(my_str)
    my_str = my_str[:my_str.index(".")] # 처음부터 점 이전까지만 추출
    pw = my_str[:3]+str(len(my_str))+str(my_str.count("o"))+str(my_str.count("k"))+"!"+"kig"
    f.write(pw + "\n")
f.close()