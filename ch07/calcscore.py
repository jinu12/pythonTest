import calc


def calcscore(name, *score, **option):
    results = {}

    total = 0
    for i in score:
        total += i

    results["name"] = name
    results['score'] = score

    # results += name + ':' + str(total)

    if option['avg']:
        results['avg'] = ':' + str(total/len(score))

    return results


def start():
    result = calcscore('kim', 98, 88, 99, avg=True)
    print('name :', result['name'])
    print('score :' + str(result['score']))
    print('avg :' + str(result['avg']))
    result2 = calc.calc(1, 2, 4, 5, 7)
    print(result2)


if __name__ == '__main__':
    start()
