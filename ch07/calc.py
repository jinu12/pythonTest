

def calc(n, *data):
    total = 0
    for i in data:
        total += i
    result = total / n
    return result


def start():
    print('start application')
    while True:
        n = input('INput num')
        if n == '0':
            break
        result = calc(int(n), 2, 4, 5, 7, 8)
        print("Result", result)
    print('stop application')


if __name__ == '__main__':
    start()
