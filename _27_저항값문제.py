import math

resistor_info = {"black":0,"brown":1,"red":2,"orange":3,"yellow":4,"green":5,"blue":6,"violet":7,"grey":8,"white":9}
first_input = input()
second_input = input()
third_input = input()

# 10 제곱 방법 math.pow(x,y) 또는 x**y
result = ((resistor_info[first_input]*10) + resistor_info[second_input]) * math.pow(10,resistor_info[third_input])
print(result)
