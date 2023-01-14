def hash_display():
    result = ""
    try:
        file = open("matter.txt", "r")
    except FileNotFoundError as e:
        print(e)
    else:
        res = file.read()
        file.close()
        for i in res:
            result += i + '#'
        return result


print(hash_display())
