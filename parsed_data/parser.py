import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver


options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('disable-gpu')
path = "/home/thecook/바탕화면/chromedriver" # 웹드라이버 경로 파일명까지
driver = webdriver.Chrome(path, chrome_options=options)             # 웹드라이버 종류 경로변수 지정
driver.implicitly_wait(2)
driver.get("http://www.vitibet.com/index.php?clanek=quicktips&sekce=fotbal&lang=en")       # 웹드라이버로 얻고싶은 주소 지정

html = driver.page_source
soup = BeautifulSoup(html, 'lxml')
football = soup.select('#quicktips > table > tbody > tr')

for data in football:
    print(data.text)


        # foot_list.append(data.text)
        # articles = pd.DataFrame(data, columns=['날짜', 'Home', 'Away', 'Score', 'Score', '승리', '무승부', '패배'])


    # search_box = driver.find_element_by_name("q") # 구글홈페이지 기준으로 개발자 도구로 검색창 input name이 q로 지정 되어있음
    # search_box.send_keys("u-20 월드컵")            # input에 u-20 월드컵 값을 보냄
    # search_box.submit()                           # submit 버튼 누름

