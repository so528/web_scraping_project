# step1.프로젝트에 필요한 패키지 불러오기

from bs4 import BeautifulSoup as bs

import requests


# step2. 검색할 키워드 입력

query = input('검색할 키워드를 입력하세요: ')


# step3. 입력받은 query가 포함된 url 주소(네이버 뉴스 검색 결과 페이지) 저장

url = 'https://search.naver.com/search.naver?where=news&sm=tab_jum&query='+'%s'%query


# step4. requests 패키지를 이용해 'url'의 html 문서 가져오기

response = requests.get(url)

html_text = response.text


# step5. beautifulsoup 패키지로 파싱 후, 'soup' 변수에 저장

soup = bs(response.text, 'html.parser')

# print(response.text)
f = open('static.html', 'w', encoding='utf-8')
f.write(response.text)

#step6.뉴스 제목 텍스트 추출

news_titles = soup.select("a.news_tit") #그래서 html의 class와id 속성이 중요하다...

for i in news_titles:
    title = i.get_text()
    print(title)