def filewrite(name, content):
    f = open(name, "wt")
    try:
        f.write(content)
    except:
        raise FileExistsError
    finally:
        f.close()


def fileread(name):
    f = open(name, 'rt')
    try:
        text = f.read()
    except FileNotFoundError as fe:
        raise fe
    except IOError as ie:
        raise ie
    finally:
        f.close()
    return text


