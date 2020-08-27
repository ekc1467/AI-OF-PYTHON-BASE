# -*- coding: utf-8 -*-
from keras.models import Sequential
from keras.layers import Dense

# 필요한 라이브러리 로딩
import numpy
import tensorflow as tf

# 실행할 때마다 같은 결과를 출력하기 위해 설정하는 부분
seed = 0
numpy.random.seed(seed)
tf.set_random_seed(seed)

# (1) 데이터 준비 ------------------------------------------
Data_set = numpy.loadtxt("../DATA/ThoraricSurgery.csv", delimiter=",")

# (2) 데이터 가공 -----------------------------------------------------
# 환자의 기록과 수술 결과를 X와 Y로 구분하여 저장
X = Data_set[:,0:17]
Y = Data_set[:,17]

# (2) 딥러닝 모델 구조 정의---------------------------------------------------
model = Sequential()
# 17개 입력  => 30개 전달
model.add(Dense(30, input_dim=17, activation='relu'))
# 1개 전달 즉 출력력model.add(Dense(1, activation='sigmoid'))

# (3) 모델 구축 ---------------------------------------------------
model.compile(loss='mean_squared_error', optimizer='adam', metrics=['accuracy'])
#model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# (4) 데이터 훈련하기 ----------------------------------------------
model.fit(X, Y, epochs=30, batch_size=10)

# (5) 테스트 데이터로 평가 -----------------------------------------
print("\n Accuracy: %.4f" % (model.evaluate(X, Y)[1]))


