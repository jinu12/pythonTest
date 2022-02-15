from math import sqrt, pow

structure = [[], [], [], [], [], [], [], [], [], []]
width = 0
length = 0
print("==========전체 셀==========")
for i in range(len(structure)):
    for j in range(len(structure)):
        structure[i].append("ㅁ")

for i in range(len(structure)):
    length += 1
    for j in range(len(structure)):
        width += 1
        print(structure[i][j], end=" ")
    print("")

width = width / len(structure)
diagonal = sqrt(pow(width, 2) + pow(length, 2))


print("전체 셀의 가로 길이 : {}m, 세로 길이 : {}m".format(width, length))
print("전체 셀의 대각선 길이 : {}m".format(diagonal))
