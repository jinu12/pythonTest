def maxmin(datas):
    """
        입력받은 데이터는 리스트 이다
        이벽받은 데이터의 최대값과 최소값을 리 턴 하ㅣ오
    """
    results = {}
    results['max'] = max(data)
    results['min'] = min(data)
    return results


if __name__ == '__main__':
    data = [5, 7, 2, 6, 2, 3, 9]
    result = maxmin(data)
    print(result['max'])
    print(result['min'])
