def JTOI():
    result = ""
    try:
        file = open("words.txt", "r")
    except FileNotFoundError as e:
        print(e)
    else:
        res = file.read()
        file.close()
        for i in res:
            if i == "J":
                result += "I"
            else:
                result += i
    return result


print(JTOI())
