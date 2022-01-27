for i in range(1, 6):
    print("파이썬 프로그래밍")

print("*"*20)

for i in range(5, 0, -1):
    print("파이썬 프로그래밍")

# 1부터  100까지의 합에서 3의 배수의 합 구하기
Sum2 = 0
Sum = 0
for i in range(0, 101, 3):
    Sum = Sum + i
    print(Sum)


for i in range(1, 100):
    if i % 3 == 0:
        Sum2 = Sum2 + i
print(Sum2)
