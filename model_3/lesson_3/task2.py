# test.txt faylda so'zlar berilgan ushbu so'zlardagi har bir harfni generator funksiya orqali oling.


def get_a_piece():
    try:
        new_file = open("test.txt", "r", encoding="utf8")
    except Exception as e:
        print(e)
    else:
        res = new_file.readlines()
        new_file.close()

        for i in res:
            for j in i:
                yield j


generator = get_a_piece()
for _ in get_a_piece():
    print(next(generator))
