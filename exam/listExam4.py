
# 1.
print("#1")
studentlist = ["장동건", "김범룡", "장기용", "이민호", "RM", "정국", "지민", "홉"]
print(studentlist)
print("*" * 60)

# 2.
print("#2")
appendlist = ['슈가', '진', '뷔']
studentlist = studentlist + appendlist
print(studentlist)
print("*" * 60)

# 3.
print("#3")
print(studentlist.index('홉'))
studentlist[7] = '제이홉'
print("*" * 60)

# 4.
print("#4")
len(studentlist)
print(studentlist[0:])
print(studentlist[::-1])
print("*" * 60)

# 5.
# sort는 리턴값이 없음
# sorteds는 리턴 값이 있음
print("#5")
studentlist.sort(reverse=True)
reverseList = sorted(studentlist, reverse=True)
print(studentlist)
print(reverseList[:])
print("*" * 60)

# 6.
print("#6")
studentlist.insert(0, '정우성' or '정기용')
print(studentlist)
print("*" * 60)

# 7.
print("#7")
print(studentlist.index('슈가'))
studentlist.insert(8, [100, 90, 80])
studentlist.insert(7, [88, 77])
print(studentlist)
print("*" * 60)

# 8.
print("#8")
studentlist[9][1] = 100
print(studentlist[9][1])
print("*" * 60)

# 9.
print("#9")
print(studentlist[9][0:])
print("*" * 60)

'''
    1. 다음과 같은 데이털르 이용하여 리스틀를 작성하세요.
       장동건, 김범룡, 장기용, 이민호, RM, 정국, 지민, 홉
    2. 슈가, 진, 뷔를 마지막에 추가해주세요.
    3. 홉의 이름을 제이홉으로 변경하기
    4. studentlist 리스트에 저장된 모든 학생을 앞에서 부터, 뒤에서 부터 각각 출력
    5. 
'''