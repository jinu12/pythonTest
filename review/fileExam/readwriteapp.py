import readwrite


def start():
    # name = input('Input File Name ..?')
    # content = input('Write Contents ..:')
    # readwrite.filewrite(name, content)
    rname = input('Input read file Name...?')
    try:
        rcontent = readwrite.fileread(rname)
        print(rcontent)
    except FileNotFoundError:
        print('파일을 찾지 못했습니다.')


if __name__ == '__main__':
    start()
