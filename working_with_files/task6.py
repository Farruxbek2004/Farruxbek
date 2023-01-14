def count_func():
    count = 0
    try:
        file = open("article.txt", "r")
    except FileNotFoundError as e:
        print(e)
    else:
        res = file.read()
        file.close()
        for i in res.split():
            if i in "this" or i in "these":
                count += 1
    return count


print(count_func())
