#-*- coding: utf-8 -*-
#0일 때 오차 그래프와 1일 때 오차그래프가 서로 다르다.57P 0일때 0 1일 때 1일이 가장적절
import tensorflow as tf
import numpy as np

# x,y의 데이터 값
data = [[2, 0], [4, 0], [6, 0], [8, 1], [10, 1], [12, 1], [14, 1]]
x_data = [x_row[0] for x_row in data]
y_data = [y_row[1] for y_row in data]
print("x = ", x_data)
print("y = ", y_data)

# a와 b의 값을 임의로 정함 (w, b)
w = tf.Variable(tf.random_normal([1], dtype=tf.float64, seed=0))
b = tf.Variable(tf.random_normal([1], dtype=tf.float64, seed=0))

# y 시그모이드 함수의 방정식
y = 1/(1 + np.e**(w * x_data + b))

# loss를 구하는 함수
loss = -tf.reduce_mean(np.array(y_data) * tf.log(y) + (1 - np.array(y_data)) * tf.log(1 - y)) #줄여가며 최적의...

# 학습률 값
learning_rate=0.5

# loss를 최소로 하는 값 찾기
gradient_decent = tf.train.GradientDescentOptimizer(learning_rate).minimize(loss)

# 학습
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())

    for i in range(60001):
        sess.run(gradient_decent)
        if i % 6000 == 0: #6000번에 한번
            print("Epoch: %.f, loss = %.4f, 기울기 w = %.4f, 바이어스 b = %.4f" % (i, sess.run(loss), sess.run(w), sess.run(b)))