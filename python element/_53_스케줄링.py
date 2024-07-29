import schedule # 스케줄기능 사용하기 위한 모듈 호출

import time   # 일정시간만큼 대기를 위해서
import requests # 서버와 http 동기 통신을 하기 위해 사용
from bs4 import BeautifulSoup #html 파싱해서 원하는 정보를 추출하기 위해 사용

def perform_web_crawling():
    url = "http://www.naver.com"
    response = requests.get(url)
    if response.status_code ==200:
        soup = BeautifulSoup(response.text, "html.parser")
    print(soup)

def job():
    print("웹 크롤링을 수행합니다.")
    perform_web_crawling()


# schedule.every().day.at("09:45").do(job) # 9:45분에 동작
schedule.every(1).minutes.do(job) # 매분에 시작
while True:
    schedule.run_pending() # 대기중인 작업을 수행하는 함수
    time.sleep(1) # 1초 대기