from time import strftime


def write_exceptions(exception, e):
    with open('exceptions.txt', 'a') as file:
        dct = {exception: e, 'data time':strftime("%Y-%m-%d %H:%M:%S") }
        file.write(f'{dct}\n')


def get_datatime():
    try:
        file = open("lesson1.txt", "r")
    except Exception as e:
        write_exceptions(Exception, e)
        with open("lesson2.txt", "a") as b:
            b.write(f"{e}")

    else:
        print(file.read())
        file.close()
    return ""


print(get_datatime())
