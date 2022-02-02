# 주어진 년도의 윤년 구하기
year = int(input("연도를 입력해주세요."))
yoon = "년 2월 말일은 29일입니다"
elseYoon = "년 2월 말일은 28일입니다"
if year % 4 == 0:
    print("{}{}".format(year, yoon))
elif year % 4 == 0 and year % 100 == 0:
    print("{}{}".format(year, elseYoon))
elif year % 100 == 0 and year % 400 == 0:
    print("{}{}".format(year, yoon))
else:
    print("{}{}".format(year, elseYoon))
