# 파이썬에서 제공되는 랜덤수를 관리하는 기능을 구현해 놓은 객체
# randomw 과 같은 다양한 기능을 구현할 수 있도록 파이썬에서는 다양한 객체를 제공
# random 객체에 정의되어 있는 기능을 활용해서 다양한 방법으로 랜덤수를 사용할 수 잇다
# choice(), randrange(), randint() .........
# random를 사용하기 위해서 rnadom이라는 모듈을 추가해야 한다. 기본으로 인식하지 못하기 때문에
# import 명령문을 사용해서 기능
import random
# 파이썬 인터프린터에 random 을 사용하겠다고 알려주는 작업
# choic([1,2,3,4,5,6])
myrandomNum = random.randrange(1, 7)
print(myrandomNum)