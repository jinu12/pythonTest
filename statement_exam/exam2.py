# 주사위 두 수의 합이 6이 되는 경우 구하기
for i in range(1, 7):
    for j in range(1, 7):
        if i + j == 6:
            print(i, j)