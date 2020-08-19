"""그림->csv파일로 만드는 코드이다.
울트라 에디터로 바이더리 데이터를 열 수 있다.
이 바이너리의 값은 사이트에서 알 수 있으며 계산기 보기에서 프로그래머 용으로 변환 후
HEX를 체크 후 확인해 볼 수 있다."""
import struct
def to_csv(name, maxdata):
    # 레이블 파일과 이미지 파일 열기
    lbl_f = open("./mnist/"+name+"-labels-idx1-ubyte", "rb")
    img_f = open("./mnist/"+name+"-images-idx3-ubyte", "rb")
    csv_f = open("./mnist/"+name+".csv", "w", encoding="utf-8")
    # 헤더 정보 읽기 --- (※1)
    mag, lbl_count = struct.unpack(">II", lbl_f.read(8)) #매직 코드 4개, 레이블 개수 4개
    #파일을 읽어 바이너리로 된 것을 쓸 수 있게 Struct로 사용.
    mag, img_count = struct.unpack(">II", img_f.read(8)) #매직코드 4개 이미지 개수 4개
    rows, cols = struct.unpack(">II", img_f.read(8))#각 행렬 개수 4개. 참고로 포인트는 이동한다.
    pixels = rows * cols #쭉 늘려 쓴다.
    # 이미지 데이터를 읽고 CSV로 저장하기 --- (※2)
    res = []
    for idx in range(lbl_count):
        if idx > maxdata: break
        label = struct.unpack("B", lbl_f.read(1))[0]
        bdata = img_f.read(pixels)
        sdata = list(map(lambda n: str(n), bdata))
        csv_f.write(str(label)+",")
        csv_f.write(",".join(sdata)+"\r\n")
        # 잘 저장됐는지 이미지 파일로 저장해서 테스트하기 -- (※3) #JPG파일로 바꿀려면 헤더를 jpg 형식으로 다 작성해야함.
        if idx < 10:
            s = "P2 28 28 255\n" #PGM 헤더이다. 파일 포맷/픽셀 행수/픽셀 열 수/최대값.
            s += " ".join(sdata)
            iname = "./mnist/{0}-{1}-{2}.pgm".format(name,idx,label)
            with open(iname, "w", encoding="utf-8") as f:
                f.write(s)
    csv_f.close()
    lbl_f.close()
    img_f.close()
# 결과를 파일로 출력하기 --- (※4)
to_csv("train", 1000)
to_csv("t10k", 500)