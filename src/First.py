import sys

A=True
name="z"
avg=23.4
age=12

print('',type(str(avg)),type(avg))
avg=str(avg)
msg="good"
print("indexing:",msg[0],msg[2],msg[-1])
#한개 한개 요소에 접근하는 방법=>인덱싱
print("sclicing=>",msg[0:3]) #[시작인덱스 : 끝인덱스+1]
print("sclicing=>",msg[2:])
print("sclicing=>",msg[:-2])
print("sclicing=>",msg[:])#모두
#특정 부분을 추출하는 방법=>슬라이싱
print(msg.count('oo'))
print(msg.upper(),msg)
print(msg.find('o'),msg.index('o')) #index는 없으면 error를 발생시킨다.
#print(msg.split('')) #지정된 문자(구분자)로 문자열 쪼개기
msg="Happy, new, year,2021,!"
print(msg.split(',')) #지정된 문자(구분자)로 문자열 쪼개기
#항상 인덱싱 슬라이싱을 한 후 사용할거면 바인딩 해두자.
msglist=msg.split(',')
print(('-').join(msglist))#지정된 문자로 문자열 합치기
#str형태를 원하는 변경을 실행하는 함수 {}.format(num)
data=['kkk',23,1.23,False]
print('data=>',data)
print(data[0],data[-1],data[0:2])
data=[] #빈리스트
data.append('DATA')
print('data =>',data)
data.append(7) #데이타 추가
print('data =>',data)
data.insert(1,True)
print('data =>',data)
data[1]=123.346 #데이터 변경이 가능
print('data =>',data)
data.pop(1)
print('data =>',data)

#변경 불가 데이터 저장 타입 ==> 튜플(tuple)
tdata=(1,2,3)
tdata2='a',12,34
tdata3='happy', #괄호를 사용하지 않을 수 있음. 한 인수만 쓸 떄 끝에 콤마를 찍어줘야 튜플타입이라고 인지.
tdata4=(1,)
#튜플은 값 변경은 불가능하다. 또한 튜플에 딕셔너리, 리스트 등 또한 삽입 가능하다. 또한 반대도 가능하다.
print('type(tdata)=>',type(data))

dic1={'name':'Tom','age':10,'birth':'1115'}
dic2={1:'hi',2:'ph'}
print(dic1['name'],dic2[1])
print(dic1.keys())
print(dic2.values())
print(dic1.items())#튜플 타입으로 가져옴.


