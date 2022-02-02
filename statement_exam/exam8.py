# 각 학생의 점수를 이차원 리스트
studentlist = [
                   ["성명", "장동건", "이민호", "김범룡"],
                   ["python", 88, 65, 82],
                   ["web", 76, 70, 80],
                   ["android", 92, 58, 78],
                   ["raspberry", 92, 82, 88],
               ]

for i in range(0, 5):
    for j in range(0, 4):
        print(studentlist[i][j])
    print("", end="")
