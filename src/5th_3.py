#setting에서도 가능하다.

# 모듈 로딩 ----------------------------------------
import yaml
# 데이터 변수 선언 ----------------------------------
yaml_str = """
Date: 2017-03-10
PriceList:
    -
        item_id: 1000
        name: Banana
        color: yellow
        price: 800
    -
        item_id: 1001
        name: Orange
        color: orange
        price: 1400
"""

# YAML 분석 -------------------------------------------
data = yaml.load( yaml_str, Loader=yaml.FullLoader )
# 이름, 가격 데이터 출력 --------------------------------
for item in data['PriceList']: #파이썬 형식으로 문장을 받았기 때문에 리스트 이용.
    print(item["name"], item["price"])