#특별한 형태의 함수
#기능: 두 개의 함수 더하기
#이름: add
#인수: a,b
#결과: 더한 결과 반환
def add(a,b):
    r=a+b
    return a+b

def add2(a,b):
    return a+b

#기능: 메시지 출력
#이름: display
#인수: msg
#결과: 없음
def display(msg):
    print('msg==>',msg) #반환 값이 없는 경우

#기능: 테스트 로그 출력 함수
#이름: testlog
#인수: 없음
#결과: 없음

def testlog():
    print('test') # 인자 값이 없다.

#함수 사용하기, 즉 함수 호출-----------------------------------------
display('Happy')
display(20)
display(False)

res=add(10,20) #인자가 있을 경우 그 개수만큼 대입을 해서 바인딩을 해주어야한다.
print("res=",res)

#가변인자 함수. 인자를 자유롭게 받을 수 있다.
def getSum(*args):
    sum=0
    for i in args:
        sum += i
    return sum

r=getSum(1,2,3,4,5,6)
print(r)

#키워드 파라미터
def printdata(**kwargs):
    print(type(kwargs))
    print(kwargs)

printdata(a=1)
printdata(name='hong',age=12,code='ko')
#인자를 키워드 파라미터 함수는 딕셔너리로 인식하기 때문에 딕셔너리 형태로 대입해도 된다

#***함수는 여러개를 반환할 때는 항상 튜플값을 반환한다.***

def cal(a,b):
    return a+b,a-b,a*b,a/b

print(cal(5,5))

#람다를 이용하면 빠르고 간단하게 함수를 이용할 수 있다.
add= lambda x,y:x+y #인자,인자:함수 공식
print(add(1,2))

cal=[lambda x,y:x+y,lambda x,y:x-y]#배열 방식으로 람다를 이용
print(cal[0](1,2))
print(cal[1](1,2))

#map(함수,리스트) 리스트의 요소를 지정된 함수로 처리하여 반환하는 함수
a=list(map(str,range(10)))

import sys
import math
import matplotlib as mp #import 모듈 as 줄임말
#from 모듈명 import 함수명1,함수명2 =>모듈의 특정 함수만 사용하겠다.
#남의 새로운 모듈을 사용하고 싶은 경우 그 사용자의 모듈을 설치하고 import module name한 후 모듈명.함수(), 모듈명.변수

sys.getrefcount(0)
math.atan2(10,2)