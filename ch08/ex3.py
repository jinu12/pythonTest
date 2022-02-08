count = 0
while True:
    st = input('input nmber')

    if st == 'q':
        print("정답입니다.")
        break
    try:
        count = count + 1
        print("실패 횟수 :", count)
    except ValueError as e:
        print('retry....')
print('Exit')