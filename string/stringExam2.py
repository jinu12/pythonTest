# eightlist = []
# count = 0
# for i in range(1, 10001):
#     eightlist.append(list(str(i)))
# for i in range(len(eightlist)):
#     for j in range(len(eightlist)):
#         for k in range(len(eightlist)):
#             for n in range(len(eightlist)):
#                 if eightlist[i][j][k][n] == 8:
#                     count = count + 1
# print(count)

count = 0

for i in range(1, 10001):
    # print("i=", i)
    for k in str(i):
        # print("k=", k)
        if k == "8":
            count = count +1

print("8의 횟수=", count)

print("*" * 70)

count2 = 0
for i in range(1, 10001):
    count2 = count2 + str(i).count("8")
print("8의 횟수=", count2)

print("*" * 70)

str1 =""
count = 0
for i in range(1, 10001):
    str1 = str(i)
    count += str1.count('8')
    if str1.count('8'):
        print(str1)

print(count)

# final = ""
# for i in range(1, 10001):
#     final = final + str(i)
#     print(final)
# print(final.count("8"))
