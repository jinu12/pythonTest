# 이차원 배열을 만들고 변경하고 출력하기
networkxtwolist = [
                   ["A", "B", "C", "D", "E"],
                   ["F", "G", "H", "I", "J"],
                   ["K", "L", "M", "N", "O"],
                   ["P", "Q", "R", "S", "T"],
                   ["U", "V", "W", "X", "Y"]
]

print("\t\t원본 배열")
print("=" * 25)
for i in networkxtwolist:
    for j in i:
        print(j, end="     ")
    print("")

# print("\t\t수정된 배열")
# print("=" * 25)
#
# for i in range(len(networkxtwolist)):
#     networkxtwolist[i][i] = "*"
# print(networkxtwolist)

# for i in networkxtwolist:
#     for j in i:
#         print(j, end="     ")
#     print("")

print("\t\t수정된 배열")
print("=" * 25)

for i in range(len(networkxtwolist)):
    for j in range(len(networkxtwolist)):
        if i != j:
            print(networkxtwolist[i][j], end="     ")
        else:
            print("*", end="     ")
    print("")
