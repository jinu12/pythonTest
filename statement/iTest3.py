print("안녕하세요 무엇을 원하신가요?")
test = bool
while test:
    case = input("1 : 점수를 확인하고 싶어요 , 2 : 점수를 조회하고 싶어요 , 3: 종료하고 싶엉요 \n입력 : ")
    if case == "1":
        print("점수를 입력해주세요")
        num = int(input("점수 : "))
        if num > 50:
            print("만족1")
        else:
            print("분발해야 할 것 같아요.")
    elif case == "2":
        print("해당 서비스는 준비중입니다.")
    else:
        print("종료되었습니다.")
        test = False
