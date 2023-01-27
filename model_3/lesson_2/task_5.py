# sum_index nomli funksiya yarating va bu funksiya faqat list qabul qilsin. Funksiya berilgan list
# indexlari yig'indisini qaytarsin. Funksiyaga beriladigan argumentni tekshirish uchun dekorator yozing.
# sum_index([2, 4, 5, 6])  # 6
# sum_index((2, 4, 5, 6))  # Please send only list.


def sum_error(func):
    def list_error(lst):
        if type(lst) == list:
            return func(lst)
        else:
            print('Please send only list.')

    return list_error


@sum_error
def sum_index(lst):
    return sum([i for i in range(len(lst))])


lst = [2, 4, 5, 5, 6]
print(sum_index(lst))
