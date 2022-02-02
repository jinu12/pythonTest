# 각 학생의 점수를 이차원 리스트 총합과 평균
total = 0
count = 0

studentlist = [
                   ["성명", "장동건", "이민호", "김범룡"],
                   ["python", 88, 65, 82],
                   ["web", 76, 70, 80],
                   ["android", 92, 58, 78],
                   ["raspberry", 98, 82, 88],
               ]

totallist = ["총점"]
avglist = ["평균"]

for i in range(1, 4):
    for j in range(1, 5):
        total = total + int(studentlist[j][i])
        count = count + 1
    totallist.append(total)
    avglist.append(total/count)
    total = 0
    count = 0

studentlist.append(totallist)
studentlist.append(avglist)


for i in range(0, 7):
    for j in range(0, 4):
        print(studentlist[i][j])
    print("")





