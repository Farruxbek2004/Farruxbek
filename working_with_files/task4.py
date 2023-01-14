def count_the():
    try:
        file = open("notes.txt", "r")
    except FileNotFoundError as e:
        print(e)
    else:
        res = file.read().lower()
        file.close()
        res.split()
        print(res.count("the"))
    return ''


print(count_the())
