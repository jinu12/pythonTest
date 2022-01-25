'''
 여러 줄 주석문 사용하기
 if문 안에서
 if문을 중첩해서 사용하기
 점수와 시험횟수를 파악하기
 점수가 60점 이상이고 시험횟수가 3이하이면 합격
'''
jumsu = 87
examcount = 4
if jumsu >= 60:
    if examcount <= 4:
        print('합격')
    else:
        print('불합격')
else:
    print('불합격')
