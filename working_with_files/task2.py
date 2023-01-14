def story_func():
    count_len = list()
    try:
        file = open("story.txt", "r")
    except FileNotFoundError as e:
        print(e)
    else:
        res = file.readlines()
        file.close()
        for index_file in res:
            if not index_file[0] == "T":
                count_len.append(index_file)

    return len(count_len)


print(story_func())
