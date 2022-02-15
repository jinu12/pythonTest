# 1부터 50까지 소수 구하기
# count = 0
# decimalList = []
# for i in range(1, 51):
#     for j in range(1, 51):
#         if i % j == 0:
#             print(j)
#             count = count + 1
#             print(count)
#             if count == 2:
#                 decimalList.append(j)
# print(decimalList)

count = 0
decimalList = []
for i in range(1, 51, 1):
    for j in range(1, 51, 1):
        if i % j == 0:
            count = count + 1
        if count == 2:
            decimalList.append(j)
            count = 0
for i in range(len(decimalList)):
    print(decimalList[i])






