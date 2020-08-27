import tensorflow as tf

# 데이터 준비 & 노드 정의 -------------------------------------
# 학습 데이터
x_data = [[1, 2],[2, 3],[3, 1],[4, 3],[5, 3],[6, 2]]#1,2를 주면0주고  2,3 주면 0 , //5, 3 주면  1주고
y_data = [[0],[0],[0],[1],[1],[1]]

# 변수
X = tf.placeholder(tf.float32, shape=[None, 2])         # 열2개인 2차원 배열 .None은 몇개가 들어올 지 몰라서..
Y = tf.placeholder(tf.float32, shape=[None, 1])         # 열1개인 2차원 배열
W = tf.Variable(tf.random_normal([2, 1]), 'weight')     # 행렬 곱하기
b = tf.Variable(tf.random_normal([1]), 'bias')          # 행렬 더하기

# 가설 정의 => 출력결과값 0 ~ 1 사이 범위 변환
hypothesis = tf.sigmoid(tf.matmul(X, W) + b)

# 비용 함수 정의 => Y가 1일때, Y가 0일때별 COST 계산
cost = -tf.reduce_mean(Y * tf.log(hypothesis) + (1 - Y) * tf.log(1 - hypothesis)) #Y=1 ,0일따의 차의 합의 평균을 비용함수에 넣는다.

# cost function 최소화
optimizer = tf.train.GradientDescentOptimizer(learning_rate=1e-2)
train = optimizer.minimize(cost)

# True if hypothesis > 0.5 else false
predicted = tf.cast(hypothesis > 0.5, dtype=tf.float32) #1 아니면 0이기때문에 트루 펄스로 떠서 FLOAT32로 바꾸고

# 정확도 체크
accuracy = tf.reduce_mean(tf.cast(tf.equal(predicted, Y), dtype=tf.float32))

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())

    for step in range(10001):
        cost_val, train_val = sess.run(
            [cost, train],
            feed_dict={X: x_data, Y: y_data}
        )
        if step % 200 == 0:
            print(step, "\tcost : ", cost_val)

    # Accuracy report
    hypo_val, predict_val, acc_val = sess.run( [hypothesis, predicted, accuracy],feed_dict={X: x_data, Y: y_data})

    print("\nHypothesis : ", hypo_val, "\nCorrect(Y) : ", predict_val, "\nAccuracy : ", acc_val)