import random
import time


def connect():
    print('Connect')


def sendData(data):
    if data == 3:
        raise IOError
    print('Send Data:', data)


def close():
    print('Closed Server ...')
    exit()


while True:
    temp = random.randint(1, 11)
    try:
        connect()
        sendData(temp)
    except:
        print('Server Error ...')
    finally:
        close()
    time.sleep(3)
