import urllib.request
import urllib.parse
try:
    #읽기모드
    file = open('test.html',mode='r',encoding='utf8')

    while True:
        line=file.readline()
        if not line:break
        print(line)
finally:
    file.close()
#############################################################
try:
    #파일이 없으면 만들고 있으면 덮어쓴다.
    file=open('data.txt',mode='w',encoding='utf8')

    for i in range(1,6):
        data='%d번째 줄\n' %i
        file.write(data)
finally:
    file.close()
#############################################################
with open('data.txt',mode='w',encoding='utf-8') as file: #더 편한 코딩 방법이다.
    for i in range(1,6):
        data = "%d번쨰 줄\n"%i
        file.write(data)
#############################################################
url = "http://uta.pw/shodou/img/28/214.png"
savename = "test.png"

urllib.request.urlretrieve(url,savename)
print("저장 완료")
#############################################################

"""
url = "http://uta.pw/shodou/img/28/214.png"
savename = "test.png"

mem = urllib.request.urlopen(url).read()

with open(savename,mode="wb") as 
    """

#############################################################
url = "http://api.aoikujra.com/ip/ini"
res = urllib.request.urlopen(url)
data = res.read()
print('type(data)=',type(data))
text = data.decode("utf-8")
print(text)

#############################################################
API=https://finance.naver.com/sise_index/sise_index.nhn?code=KOSPI
values={'stnld':'108'}
params = urllib.parse.urlencode(values)
url = API+"?"+params
print("url=",url)
data = urllib.request.urlopen(url).read()
text = data.decode("utf-8")
print(text)
#############################################################