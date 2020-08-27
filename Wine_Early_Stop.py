from keras.models import Sequential
from keras.layers import Dense
from keras.callbacks import EarlyStopping
import pandas as pd
from keras.utils import np_utils
#데이터 준비
df_pre = pd.read_csv('../DATA/winequality-red.csv', sep=';', header=None)
df = df_pre.sample(frac=0.15)
#데이터 가공
dataset = df.values
X = dataset[:,0:11]
Y = dataset[:,11]
print(Y)
#원 핫 인코딩으로 변환
y_nums = np_utils.to_categorical(Y, 10)

for i in range(y_nums.shape[0]):
    print(i, " => ", y_nums[i])
#딥러닝 모델 설계
model = Sequential()
model.add(Dense(30, input_shape=(11,), activation='relu'))
#model.add(Dense(12, activation='relu'))
#model.add(Dense(12, activation='relu'))
#model.add(Dense(8,  activation='relu'))
#model.add(Dense(1,  activation='sigmoid'))
model.add(Dense(10,  activation='softmax'))

#딥러닝 모델 생성
model.compile(loss='binary_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])

# 힉습준비->자동 중단 설정. 문제가 생기거나 확률이 올라가지 않을 경우
early_stopping_callback = EarlyStopping(monitor='val_loss', patience=100)

# 학습 모델 실행
model.fit(X, y_nums,
                  epochs=2000,
                  batch_size=500,
                  callbacks=[early_stopping_callback])

# 결과 출력
print("\n Accuracy: ", (model.evaluate(X, y_nums)))
