def creat_file(filepath, data):
    with open(filepath, "w") as file:
        file.write(data)


book_data = """
123, A, AA, 1000
124, B, BB, 1001
125, S, SS, 1002
"""
creat_file("Book.txt", book_data)
