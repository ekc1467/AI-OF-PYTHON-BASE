#모듈 로딩------------------------------------------------- xml_read.py
from bs4 import BeautifulSoup
import urllib.request as req
import os.path
#변수선언 -------------------------------------------------------------------
url = "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108"
savename = "../DATA/forecast.xml"#XML로 저장할 것이다. 상대경로(..개를 앞에 붙인다)
# WEB 데이터 다운로드 후 파일 저장 ---------------------------------------
if not os.path.exists(savename): #Boolean 타입이 아니라 not형식으로 들어온다.
    req.urlretrieve(url, savename) #만들었다.
# WEB 데이터 분석 ---------------------------------
xml = open(savename, "r", encoding="utf-8").read()
soup = BeautifulSoup(xml, 'html.parser')


info = {} #딕셔너리로 받는다.
for location in soup.find_all("location"):
    name = location.find('city').string
    weather = location.find('wf').string

    if not (weather in info): #키는 중복되지 않는다.
        info[weather] = []
    info[weather].append(name)
# 각 지역의 날씨를 구분해서 출력 ------------------------------------------------
for weather in info.keys():
    print("+", weather)
    for name in info[weather]:
        print("| - ", name)


