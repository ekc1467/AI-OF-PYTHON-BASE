# 모듈로딩--------------------------------------------json
import json
# 번수 선언 -------------------------------------------
data={
    'date':'2020-01-01',
    'price':{
        'apple':500, 'banana':2500
}}
savename = "../DATA/jdata.json"
# JSON형식 저장 ---------------------------------------
jdata = json.dumps(data)
# JSON 파일 생성 --------------------------------------
with open(savename,mode='w', encoding='utf-8') as file: #파일이라는 이름으로.
    file.write(jdata)