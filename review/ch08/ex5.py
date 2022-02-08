import random
import time


def connect(num):
    if num == 5:
        print('Connected')
        return 1
    else:
        raise IOError


try:
    n = random.randint(1, 10)
    connect(n)
except:
    while True:
        try:
            n = random.randint(1, 10)
            result = connect(n)
            if result == 1:
                break
        except:
            print('retry')
            time.sleep(3)

print('On going....')
