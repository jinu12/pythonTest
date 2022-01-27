# 문장을 5번 출력하기
i = 0
while i <= 5:
    print("%d : 지금은 python 기본을 학습하는중 %d", i)
    i = i + 1

# python의 while문은 else문과 함께 사용할 수 있다.
num = 1
while num <= 9:
    print("test: %d" % num)
    num = num + 1
else:
    print("종료")
print("투표종료")
