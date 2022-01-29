studylist = ["성명", ["python", "web", "android", "raspberry"],
             "장동건", [88, 76, 92, 98],
             "이민호", [65, 70, 58, 82],
             "김범룡", [82, 80, 78, 88]
             ]

print(dir(studylist))

print(studylist[3][0])

for i in studylist:
    for j in i:
        print(j, end=" ")
    print("")

print("*" * 60)
Sum = 0

for i in range(len(studylist)):
    print(i, end=" ")
    for j in range(len(studylist)):
        if i >= 3 and i % 2 == 1 and j < 4:
            print(int(studylist[i][j]))
            Sum = Sum + int(studylist[i][j])
    print("")
print("총점 :  {}".format(Sum))


