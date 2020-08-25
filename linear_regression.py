# -*- coding: utf-8 -*-

import tensorflow as tf

# (1) 노드 정의 ---------------------------------
# 선형회귀 모델(Wx + b)을 정의
W = tf.Variable(tf.random_normal(shape=[1]))   #처음 딥러닝하는 랜덤값이다.
b = tf.Variable(tf.random_normal(shape=[1]))

#데이터&라벨 저장 공간 확보
x = tf.placeholder(tf.float32)
y = tf.placeholder(tf.float32)

# 선형회귀 모델 연산 정의
linear_model = W*x + b

# 손실 함수 정의 - MSE 손실합수, Square Error
loss = tf.reduce_mean(tf.square(linear_model - y))

# 최적화를 위한 그라디언트 디센트 옵티마이저 정의
# 러닝 레이트 => 학습 속도 설정
optimizer = tf.train.GradientDescentOptimizer(0.01)
train_step = optimizer.minimize(loss)#loss를 부르고 loss가 lenearmodel을 부르고 lenearmodel이 x,y값이 필요하니 feed_dict로 값을 넣는다.

# 트레이닝을 위한 입력값과 출력값을 준비
x_train = [1, 2, 3, 4]
y_train = [2, 4, 6, 8]

# (2) 세션 실행하고 파라미터(W,b)를 noraml distirubtion에서 추출한 임의의 값으로 초기화
sess = tf.Session()
sess.run(tf.global_variables_initializer())  # random_normal()에서 임의의 값으로 변수 초기값 할당


# (3) 모델 학습 실행 : 경사하강법을 1000번 수행하면서 최적의 w,b값을 찾는다.
for i in range(1000): #처음 랜덤값을 시작으로 미분을 계산하여 최적의 w,b를 찾는다. 우리가 직관적과 논리적으로 2는4이다 가 아니라 경험들을 쌓아서 2는 4이다를 도축
  sess.run(train_step, feed_dict={x: x_train, y: y_train})  # 입력 데이터 지정
  print(i, sess.run(loss, feed_dict={x: x_train, y: y_train}), sess.run(W), sess.run(b))

# (4) 테스트 진행
x_test = [3.5, 5, 5.5, 6]
# 테스트 데이터를 이용해 학습된 선형회귀 모델이 데이터의 경향성(y=2x)을 잘 학습했는지 측정
# 예상되는 참값 : [7, 10, 11, 12]
print(sess.run(linear_model, feed_dict={x: x_test}))

# (5) 종료
sess.close()