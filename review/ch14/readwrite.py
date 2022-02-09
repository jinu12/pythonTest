def filewrite(name, content):
    f = None
    try:
        f = open(name, "wt")
        f.write(content)
    except:
        raise FileExistsError
    finally:
        if f is not None:
            f.close()


def fileread(name):
    f = None
    try:
        f = open(name, 'rt')
        text = f.read()
    except FileNotFoundError as fe:
        raise fe
    except IOError as ie:
        raise ie
    finally:
        if f is not None:
            f.close()
    return text

