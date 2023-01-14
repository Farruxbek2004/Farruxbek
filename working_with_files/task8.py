def get_is_upper():
    count = 0
    try:
        file = open("lower.txt", "r")
    except FileNotFoundError as e:
        print(e)
    else:
        res = file.read()
        file.close()
        for i in res:
            if i.isupper():
                count += 1
    return count


print(get_is_upper())
