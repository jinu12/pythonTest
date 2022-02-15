from itemModel import Item
from itemdb import ItemDb


def start():
    itemdb = ItemDb('shopdb')
    print('start App')

    print(" " * 30, end="")
    print('Start App')
    print(" " * 30, end="")
    print("")

    while True:

        print("*" * 70)
        cmd = input('Input CMD(q,i,s,so,u,d)\n입력 :')

        if cmd == 'q':
            break

        elif cmd == 'i':

            print("*" * 70)
            print('입력값 넣기')
            ids = int(input('id : '))
            names = input('이름 : ')
            price = int(input('가격 : '))
            rate = float(input('비율 : '))

            try:
                item = Item(ids, names, price, rate)
                itemdb.insert(item)
                print('입력되었습니다')
            except:
                print('Insert Error')
                print("입력이 안됬습니다. 다시 시도해주세요.")
                raise

        elif cmd == 's':

            print("*" * 70)
            selects = int(input('모두 조회 1, id, name, price 만 출력 2\n입력 :'))

            if selects == 1:
                try:
                    print('조회되었습니다')
                    datas = itemdb.select()
                    for data in datas:
                        print('%d %s %d %f' % data)

                except:
                    print('Select Error')
                    print("조회가 안됬습니다. 다시 시도해주세요.")
                    raise

            elif selects == 2:
                try:
                    for data in itemdb.select():
                        print("%d %s %s " % (data[0], data[1], data[2]))

                    print('조회되었습니다')
                except:
                    print('Select Error')
                    print("조회가 안됬습니다. 다시 시도해주세요.")
                    raise

        elif cmd == 'so':

            print("*" * 70)
            print('검색')
            ids = int(input('id : '))

            try:
                itemdb.selectOne(ids)
                print('조회되었습니다')
            except:
                print('Select Error')
                print("조회가 안됬습니다. 다시 시도해주세요.")
                raise

        elif cmd == 'u':

            print("*" * 70)
            print('업데이트')
            ids = int(input('업데이트할 id : '))
            names = input('이름 : ')
            price = int(input('가격 : '))
            rate = float(input('비율 : '))

            try:
                item = Item(ids, names, price, rate)
                itemdb.update(item)
                print('입력되었습니다')
            except:
                print('Update Error')
                print("업데이트가 안됬습니다. 다시 시도해주세요.")
                raise

        elif cmd == 'd':

            print("*" * 70)
            print('Delete Item')
            ids = int(input('삭제 id : '))

            try:
                itemdb.delete(ids)
                print('삭제되었습니다')
            except:
                print('Delete Error')
                print("삭제가 안됬습니다. 다시 시도해주세요.")
                raise

        else:
            print('올바른 단어를 입력해주세요')

    print('End App')


if __name__ == '__main__':
    start()
