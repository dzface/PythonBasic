# 딕셔너리 : {Key: Value} 로 이루어져 있음 자바의 HashMap과 동일 구조

dict = {"정경수":90,"고유림":88,"나희도":89}
print(dict.keys())
print(dict.values())
print(dict.items())

print("고유림"in dict) # key 값이 있는지 찾는 법
print(88 in dict) # value 값 확인
if "고유림"in dict:
    print(dict["고유림"])


