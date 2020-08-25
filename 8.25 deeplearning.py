import tensorflow as tf
# (1)노드 정의 ---------------------------------
a = tf.placeholder( tf.int32, [5] ) # 플레이스홀더 노드 정의
two = tf.constant(2) # 상수 노드 정의
x2_op = a * two # 연산 노드 정의
# (2) 세션 생성 ---------------------------------
sess = tf.Session()
# (3) 플레이스홀더 값 넣어 실행-----------------
#()인자에 함수,만든 플레이스 홀더에 넣을 값들.
res1 = sess.run(x2_op, feed_dict={ a: [1, 2, 3, 4, 5] })
res2 = sess.run(x2_op, feed_dict={ a: [5, 6, 7, 10, 100] })
print( 'res1={}, res2={}'.format(res1, res2) )
# (4) 세션 종료 ---------------------------------
sess.close()

'''with tf.Session() as sess:
tf.global_variables_initializer( ) # 변수 초기화 및 값 할당 #CLOSE를 사용할 필요가 없다.
앞의 구문을 제외하고 SESSION부분만 넣으면 된다.
post_var = sess.run(var)'''

''' 처음 변수 초기화 함수이다.1번
tf.random_normal 정규분포, 지정된 범위 내 임의의 값 추출
tf.truncated_normal 절단정규분포, 분포 끝부분이 잘린 임의의 값 추출
tf.random_uniform 균등 분포, 임의의 값 추출'''

'''# MSE
loss = tf.reduce_mean( tf.square( y_true - y_pred ) )
OR  제곱하는 것 같다. 최적화 함수이다. 2번.
loss = tf.losses.mean_squared_error( y_true, y_pred )'''

'''# learning_rate 속도로 W값 찾기
optimizer = tf.train.GradientDescentOptimizer( learning_rate )
# 최소비용이 되도록 w와 b 업데이트 
train = optimizer.minimize( loss )  속도조절이다.3번째 '''