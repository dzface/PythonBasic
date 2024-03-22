## 파일 생성 구조
# 파일객체 = opne(파일명, 파일모드, 인코딩)

# ## 파일 생성
# score_file = open("./score.txt","w", encoding="utf-8")
# print("수학 : 55",file=score_file)
# print("영어 : 60",file=score_file)
# score_file.write("과학 : 90\n")
# score_file.write("국어 : 99\n")
# score_file.close()

# # 파일 읽기
# score_file = open("./score.txt","w", encoding="utf-8")
# # read() 함수 : 파일 내의 모든 내용을 읽어 하나의 문자열로 반환
# print(score_file.read())
# score_file.close()
# while True:
#     line = score_file.readline()
#     if not line : break
#     print(line, end="")
# score_file.close()
#
# # readlines(): 해당 파일의 모든 라인을 순서대로 읽어 리스트로 반환
# lines =score_file.readlines() # 파일의 라인을 리스트로 반환
# for line in lines:
#     print(line, end="")
#
# score_file.close()

# with 구문을 사용하면 구문이 종료 될 때 자동으로 파일을 닫음
# with open("./score.txt", "r", encoding="utf-8") as score_file:
#     lines = score_file.readlines()
#     for line in lines:
#         print(line, end="")

test_file = open("./test.txt","w",encoding="utf-8")
print("테스트" , file=test_file)
print("연습", file=test_file)
test_file.close()