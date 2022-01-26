"""
    입력 받은 값을 평가하여 값을 출력하시요
  [조건]
  - 나이와 성별을 각각 입력받는다. (변수명은 임의로 정의)
  - 입력받은 아이와 성별을 출력하기
  - 입력 받은 값을 평가해서 출력(if문을 중첩해서 사용하기)
    1) 나이가 20이상 성별 1 => 성인 남자
    2) 나이가 20이상 성별 2 => 성인 여자
    3) 나이가 20미만 성별 1 => 청소년 남자
    4) 나이가 20미만 성별 2 => 청소년 여자
"""

test = bool
while test:
    case = input('세대 구문 : 1, 종료 : 2\n')
    if case == "1":
        age = int(input('나이를 입력해주세요 : '))
        human = int(input('성별을 입력해수제요 : '))
        if age >= 20:
            if human == 1:
                print("성인 남자")
            elif human == 2:
                print("성인 여자")
        else:
            if human == 1:
                print("청소년 남자")
            elif human == 2:
                print("청소년 여자")
    elif case == "2":
        print("종료되었습니다.")
        test = False
    else:
        print("정확한 숫자를 입력해수에용")
