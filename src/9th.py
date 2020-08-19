from sklearn import model_selection, svm, metrics
# CSV 파일을 읽어 들이고 가공하기 --- (※1)
def load_csv(fname):
    labels = []
    images = []
    with open(fname, "r") as f:
        for line in f:
            cols = line.split(",")
            if len(cols) < 2: continue #라인 구분문자는 데이터가 아니므로 스킵
            labels.append(int(cols.pop(0))) #데이터 리스트 첫번째 요소 꺼내기
            vals = list(map(lambda n: int(n) / 256, cols)) #784개 이미지 리스트
            images.append(vals) #이미지 데이터 저장.
            #딕셔너리 타입으로 반환
    return {"labels":labels, "images":images}

#학습 및 테스트용 데이터 로딩
data = load_csv("./mnist/train.csv") #딕셔너리 타입 학습 데이터 로딩
test = load_csv("./mnist/t10k.csv") #딕셔너리 타입 테스트 데이터 로닝
# 학습하기 --- (※2)
clf = svm.SVC()
clf.fit(data["images"], data["labels"])
# 예측하기 --- (※3)
predict = clf.predict(test["images"])
# 결과 확인하기 --- (※4)
ac_score = metrics.accuracy_score(test["labels"], predict)
cl_report = metrics.classification_report(test["labels"], predict)
print("정답률 =", ac_score)
print("리포트 =")
print(cl_report)