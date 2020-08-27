from keras.models import Sequential
from keras.layers.core import Dense, Dropout, Activation
from keras.callbacks import EarlyStopping
import pandas as pd, numpy as np

# (1) 데이터 준비 --------------------------------------------------
# BMI 데이터를 읽어 들이고 정규화
csv = pd.read_csv("../DATA/bmi.csv")

# (2) 데이터 가공 --------------------------------------------------
# 몸무게와 키 데이터
csv["weight"] /= 100
csv["height"] /= 200

# DataFrame -> matrix로 변환
X = csv[["weight", "height"]]
# 레이블
bclass = {"thin":[1,0,0], "normal":[0,1,0], "fat":[0,0,1]}
#위의 레이블이 2만개 있어야한다.
y = np.empty((20000,3))
for i, v in enumerate(csv["label"]):
    y[i] = bclass[v]

# (3) 훈련 전용 데이터와 테스트 전용 데이터로 나누기 -----------
X_train, y_train = X[1:15001], y[1:15001]
X_test,  y_test  = X[15001:20001], y[15001:20001]

# (4) 모델 구조 정의하기 ------------------------------------
model = Sequential()
model.add(Dense(512, input_shape=(2,)))     # 입력층
model.add(Activation('relu'))
model.add(Dropout(0.1))
model.add(Dense(512))                       # 은닉층
model.add(Activation('relu'))
model.add(Dropout(0.1))
model.add(Dense(3))                         # 출력층
model.add(Activation('softmax'))

# (5) 모델 구축하기 ----------------------------------------
model.compile(
    loss='categorical_crossentropy',
    optimizer="rmsprop", #원하는 옵티마이저 고르기. rmsprop.
    metrics=['accuracy'])

# (6) 데이터 훈련하기 -----------------------------------------
hist = model.fit(
    X_train, y_train,
    batch_size=100,
    nb_epoch=20,
    validation_split=0.1,
    callbacks=[EarlyStopping(monitor='val_loss', patience=2)],
    verbose=1) #로스률을 보고 멈추겠다.
# (7) 테스트 데이터로 평가하기 -------------------------------------
score = model.evaluate(X_test, y_test)
print('loss=', score[0])
print('accuracy=', score[1])