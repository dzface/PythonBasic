
test = open("Good.txt", "w",encoding="utf-8")
print("테스트", file=test)
test.write("1234")
test.close()