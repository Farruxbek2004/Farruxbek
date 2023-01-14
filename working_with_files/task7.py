def count_e():
    count_len = 0
    try:
        file = open("file.txt", "r")
    except FileNotFoundError as e:
        print(e)
    else:
        res = file.read()
        file.close()
        for i in res.split():
            if i[-1] == "e":
                count_len += 1
    return count_len


print(count_e())
