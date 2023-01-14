def display_words():
    word = list()
    try:
        file = open("story.txt", "r")
    except FileNotFoundError as e:
        print(e)
    else:
        res = file.read()
        file.close()
        for index in res.split():
            if len(index) < 4:
                word.append(index)
        return word


print(display_words())
