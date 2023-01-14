def EUCount():
    count_a = 0
    count_m = 0
    try:
        file = open("story.txt", "r")
    except FileNotFoundError as e:
        print(e)
    else:
        res = file.read().lower()
        file.close()
        for i in res:
            if i == "a":
                count_a += 1
            if i == "m":
                count_m += 1
        return f"A or a:{count_a}\nM or m:{count_m}"


print(EUCount())
