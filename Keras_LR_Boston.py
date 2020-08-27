#-*- coding: utf-8 -*-
from keras.models import Sequential
from keras.layers import Dense
from sklearn.model_selection import train_test_split

import numpy
import pandas as pd
import tensorflow as tf

# seed 값 설정
seed = 0
numpy.random.seed(seed)
tf.set_random_seed(seed)



# (1) MNIST 데이터 읽어 들이기 ------------------------------------------
df = pd.read_csv("../DATA/housing.csv", delim_whitespace=True, header=None)
'''
print(df.info())
print(df.head())
'''

# (2) 데이터 가공 -----------------------------------------------------
dataset = df.values
X = dataset[:,0:13]
Y = dataset[:,13]

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=seed)

# (2) 모델 구조 정의---------------------------------------------------
model = Sequential()
#입력층
model.add(Dense(30, input_dim=13, activation='relu'))

#은닉층
model.add(Dense(6, activation='relu'))

#출력층
model.add(Dense(1))

# (3) 모델 구축 ---------------------------------------------------
model.compile(loss='mean_squared_error',
              optimizer='adam')

# (4) 데이터 훈련하기 ----------------------------------------------
model.fit(X_train, Y_train, epochs=200, batch_size=10)

# (5) 테스트 측 값과 실제 값의 비교 평가 -----------------------------------------
Y_prediction = model.predict(X_test).flatten()
for i in range(10):
    label = Y_test[i]
    prediction = Y_prediction[i]
    print("실제가격: {:.3f}, 예상가격: {:.3f}".format(label, prediction))

