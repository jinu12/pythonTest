ssn = int(input(" 성별 코드: "))

if ssn == 1:
    print("남자")
elif ssn == 2:
    print("남자")
elif ssn == 3:
    print("남자")
elif ssn == 4:
    print("여자")
else:
    print("다시 작업")

# 논리연산자를 이용해서 작업
if ssn == 1 or ssn == 3:
    print("남자")
elif ssn == 3 or ssn == 4:
    print("여자")
else:
    print("기타")
