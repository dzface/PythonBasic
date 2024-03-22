

file_name = "스타벅스일매출.txt"
f = open(file_name,"r",encoding="utf-8")

header = f.readline() # 데이터의 첫 번째 줄을 읽음
header_list = header.split()
espresso = []
americano = []
cafelatte = []
cappucino = []

for line in f:
    data_list = line.split()
    espresso.append(int(data_list[1]))
    americano.append(int(data_list[2]))
    cafelatte.append(int(data_list[3]))
    cappucino.append(int(data_list[4]))
f.close()
print(f"{header_list[1]} 전체판매량 : {sum(espresso)}, 일평균 판매량 : {sum(espresso)/len(espresso)}")
print(f"{header_list[2]} 전체판매량 : {sum(americano)}, 일평균 판매량 : {sum(americano)/len(americano)}")
print(f"{header_list[3]} 전체판매량 : {sum(cafelatte)}, 일평균 판매량 : {sum(cafelatte)/len(cafelatte)}")
print(f"{header_list[4]} 전체판매량 : {sum(cappucino)}, 일평균 판매량 : {sum(cappucino)/len(cappucino)}")
