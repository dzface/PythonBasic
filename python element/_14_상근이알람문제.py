'''
알람 45분 일찍 설정하기
### [입력]

첫째 줄에 두 정수 H와 M이 주어진다.
(0 ≤ H ≤ 23, 0 ≤ M ≤ 59) 그리고 이것은 현재 상근이가 설정한 놓은 알람
 시간 H시 M분을 의미한다.

입력 시간은 24시간 표현을 사용한다.
24시간 표현에서 하루의 시작은 0:0(자정)이고,
끝은 23:59(다음날 자정 1분 전)이다.
시간을 나타낼 때, 불필요한 0은 사용하지 않는다.

### [출력]

첫째 줄에 상근이가 창영이의 방법을 사용할 때,
설정해야 하는 알람 시간을 출력한다.
(입력과 같은 형태로 출력하면 된다.)

'''
# 시간을 실수로 환산
old_alarm = list(map(int,input("시 분을 입력하세요. : ").split()))
hour = int(old_alarm[0]) # 입력 시간
minute = float(old_alarm[1]) # 입력 분
f_time = hour + float(minute/60)
S_TIME = 0.75 # 적용해야 할 45분 환산
f_new_alalm = f_time - S_TIME
last_time = int(f_new_alalm)
last_minute = float(f_new_alalm - last_time)*60 # 실수 분을 분으로 환산
print(f" 새로운 알람시간은 {last_time} 시 {int(last_minute)} 분 입니다.")