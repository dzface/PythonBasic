
# 파이썬의 변수는 함수 스코프 따름,
# 전역에서 선언된 변수 중 immutable 특성을 가진 경우에는 global 키워드를 사용해야 함
# 대부분의 경우에서는 전역 변수를 사용하는 것보다 매개변수로 전달하는 것이
# 문제(Side effect)발생 확률을 줄일 수 있음

knife = 10
def game(player):
    global knife
    knife -= player
    print(f"남아 있는 칼은 {knife}자루 입니다.")

def game2(plater, knife):
    knife -= plater
    print(f"남아 있는 칼은 {knife}자루 입니다.")

player = int(input("경기에 참여하는 선수가 몇명 입니까?"))
# game(player) knife 를 전역변수로 사용 하는 방법 문제 발생 소지가 있음
game2(player, knife) # knife 를 매개변수로 사용 하는 방법