# 소수 여부 판별하기
count = 0
num = int(input("2~ 100 사이의 정수를 입력하세요 :"))
for i in range(1, num + 1, 1):
    if num % i == 0:
        count = count + 1
if count == 2:
    print("{}는(은) 소수입니다.".format(num))
else:
    print("{}는(은) 소수가 아닙니디.".format(num))
