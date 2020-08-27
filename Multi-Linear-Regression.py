#-*- coding: utf-8 -*-
import tensorflow as tf

#다중 조건 선형회귀(3차원으로 나옴)
# x1, x2, y의 데이터 값
data = [[2, 0, 81], [4, 4, 93], [6, 2, 91], [8, 3, 97]]

x1 = [x_row1[0] for x_row1 in data]
x2 = [x_row2[1] for x_row2 in data]                     # 새로 추가되는 값
y_data = [y_row[2] for y_row in data]
print("x1 =", x1)
print("x2 =", x2)
print("y_data =", y_data)

# 기울기 a와 y절편 b의 값 임의 설정
# 단 기울기의 범위는 0-10 사이, y 절편은 0-100사이에서 변하게 함
# 실행 시간 오래 걸림
a1 = tf.Variable(tf.random_uniform([1], 0, 10,  dtype=tf.float64, seed=0))  # x1 기울기
a2 = tf.Variable(tf.random_uniform([1], 0, 10,  dtype=tf.float64, seed=0))  # x2 기울기
b = tf.Variable(tf.random_uniform([1],  0, 100, dtype=tf.float64, seed=0))  # y절편

# 새로운 방정식
y = a1 * x1 + a2 * x2+ b

# 텐서플로 RMSE 함수
rmse = tf.sqrt(tf.reduce_mean(tf.square( y - y_data )))#원래값 y_data와의 오차의 제곱의 근

# 학습률 값
learning_rate = 0.01

# RMSE 값을 최소로 하는 값 찾기
gradient_decent = tf.train.GradientDescentOptimizer(learning_rate).minimize(rmse)

# 학습이 진행되는 부분=================================================================
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())

    for step in range(2001):
        sess.run(gradient_decent)
        if step % 100 == 0:
            print("step: %.f, RMSE = %.04f, 기울기 a1 = %.4f, 기울기 a2 = %.4f, y절편 b = %.4f" % (step,sess.run(rmse),sess.run(a1),sess.run(a2),sess.run(b)))