# planets ushbu fayldagi ma'lumotlardan faqat name olish uchun generator yozing.
# planets_gen = gen_func()
# print(next(planets_gen))  # Mercury
# print(next(planets_gen))  # Venus
# print(next(planets_gen))  # Earth
# print(next(planets_gen))  # Mars
def get_name_txt():
    try:
        file = open("planets.txt", "r", encoding="utf8")
    except FileNotFoundError as e:
        print(e)
    else:
        result = file.readlines()
        file.close()
        for i in result:
            if "name" in i:
                yield i.split("=")[1][:-1]


planets_gen = get_name_txt()
for _ in get_name_txt():
    print(next(planets_gen))
