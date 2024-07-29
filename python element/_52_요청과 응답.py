import requests
from bs4 import BeautifulSoup
res = requests.get("http://naver.com")
print("응답 코드 : ", res.status_code)

# if res.status_code == 200:
#     print("정상 응답 입니다.")
# else :
#     print("네트워크 오류 : [에러코드 ", res.status_code, "]")

# print(res.text)
# soup = BeautifulSoup(res.text, "lxml")
# print(soup.find(attrs={"class":"notify_area"}))

html_doc ='''
<html>
  <head>
    <title>Example Page</title>
  </head>
  <body id="container'>
  <div class="example">여기는 example인 클래스 입니다.</div>
    <h1>Hello, Beautiful Soup!</h1>
    <div class="content">
      <p>This is a paragraph.</p>
      <p>This is another paragraph.</p>
    </div>
    <div id="parent">
        <div class="child">첫번째 자식 </div>
        <div class="child">두번째 자식 </div>
    </div>
    <a href="https://www.example.com">Link</a>
  </body>
</html>
'''
soup = BeautifulSoup(html_doc, 'html.parser')
print(soup)

# print(soup)
# 타이틀 태그를 검색
title_tag = soup.title
print(title_tag)

# 클래스가 "content인 div 태그 검색(CSS 선택자를 이용하여 태그를 추출)
div_tags =soup.select('div.content')
for div in div_tags:
    print(div)

#href 속성이 있는 모든 a 태그 검색
a_tags = soup.find_all('a', href=True)
for a in a_tags:
    print(a)

# Tag 객체 다루기 : Tag 객체에서는 요소의 이름, 속성, 내용 등을 다룸
tag_name = title_tag.name
print(tag_name)

# Tag 객체에서 요소의 속성얻기
tag_attrs = div_tags[0].attrs
print(tag_attrs)

# Tag 객체에서 요소의 내용 얻기
tag_content = div_tags[0].text
print(tag_content)  # 'This is a paragraph.\nThis is another paragraph.'

# CSS 선택자로 요소 검색하기
div_tags = soup.select('div.example')
print(div_tags)

# id 선택자로 요소 검색하기
id_sel = soup.select_one("#container")
print(id_sel)

# 자식태그 선택자
children = soup.select("#parent > .child")

# 속성으로 요소 검색하기
attrs = {"class": "example"}
el = soup.find_all(attrs=attrs)
print(el)

