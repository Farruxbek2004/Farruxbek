def poem_functional():
    try:
        file = open("poem.txt", 'r')
    except FileNotFoundError as e:
        print(e)
    else:
        print(file.read())
        file.close()
        return ''


print(poem_functional())
