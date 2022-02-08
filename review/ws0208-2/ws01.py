# 1 ~ 100 까지의 숫자 중 3의 배수의 합과 7의 배수의 합의 차를 구하시오.
three = 0
seven = 0
for i in range(1, 101):
    if i % 3 == 0:
        three = three + i
    elif i % 7 == 0:
        seven = seven + i
print("3의 배수의 합 :", three)
print("3의 배수의 합 :", seven)
print("3의 배수의 합과 7의 배수의 합의 차 : {}".format(three - seven))