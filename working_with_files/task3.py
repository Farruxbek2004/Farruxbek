def word_count():
    count_word = list()
    try:
        file = open("task_file", "r")
    except FileNotFoundError as e:
        print(e)
    else:
        res = file.read()
        file.close()
        for index in res.split():
            count_word.append(index)
    return f"size : {len(count_word)}"


print(word_count())
