# 두 사람이 주사위를 던져서 큰수가 나오면 이기도록 프로그램을 작성하세요
# - 랜덤수를 입력 받아서 작업하기(두 개)
# [ 출력형태]
# A의 주사위 숫자
# B의 주사위 숫자
# 결과 :
import random

numA = random.randrange(1, 7)
numB = random.randrange(1, 7)
if numA < numB:
    print("A는 %d, B는 %d, B가 이겼습니다." % (numA, numB))
elif numA > numB:
    print("A는 %d, B는 %d, A가 이겼습니다." % (numA, numB))
else:
    print("A는 %d, B는 %d, 비겼습니다." % (numA, numB))
