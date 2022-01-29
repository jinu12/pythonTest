answer = 0
while True:
    print("-----Menu--------------")
    print("1. 가정용 (liter당 50원)")
    print("2. 가정용 (liter당 45원)")
    print("3. 가정용 (liter당 30원)")
    print("0. 종료")
    print("-----------------------")

    Menu = int(input("메뉴를 선택하세요=>\n-----------------------\n"))
    if Menu == 0:
        break
    print("사용량을 입력하세요=>")
    Usage = int(input(""))
    if Menu == 1:
        answer = Usage * 50
    elif Menu == 2:
        answer = Usage * 40
    elif Menu == 3:
        answer = Usage * 35
    print("==============")

    print("사용자코드 : {}" .format(Menu))
    print("사용자코드 : {}" .format(answer))
    print("사용자코드 : {}".format(answer + answer * 0.05))