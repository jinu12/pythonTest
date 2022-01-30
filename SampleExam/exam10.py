# 임의의 정수를 입력 받아서 1 부터 1000까지의 수 중에서 입력받은 정수의 배수의 개수와 배수들의 합을 계산하십시오.
randomNumber = int(input("양의 정수를 입력하세요 :"))
randomSum = 0
randomCount = 0
for i in range(randomNumber, 1001, randomNumber):
    randomSum = randomSum + i
    randomCount = randomCount + 1
    print(i)

print("배수갯수 ={}".format(randomSum))
print("7의 배수의 합 = {}".format(randomCount))