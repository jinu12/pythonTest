# ws02
# 직사각형 가로 세로를 입력 받는다.
import math
while True:
    width = int(input('가로 :'))
    if width < 0:
        print('에러')
        break
    vertical = int(input('가로 :'))
    if vertical < 0:
        print('에러')
        break
    remainder = math.sqrt((width ** 2) + (vertical ** 2))
    print("나머지 한변은", remainder)