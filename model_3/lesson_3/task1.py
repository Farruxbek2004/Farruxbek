# 1 dan 20 gacha sonlarni toq bo'lsa o'zi, juft bo'lsa (-) operator qo'ygan holda
# a. iterator
# b. generator funksiya
# orqali chiqaring.
# my_generator = gen_func()
# print(next(my_generator))  # 1
# print(next(my_generator))  # -2
# print(next(my_generator))  # 3
# print(next(my_generator))  # -4


def odd_and_couple_check():
    for i in range(1, 21):
        if i % 2 != 0:
            yield i
        else:
            yield i * (-1)


value = odd_and_couple_check()
for _ in odd_and_couple_check():
    print(next(value))


def iterator_func():
    result = []
    for i in range(1, 21):
        if i % 2 == 0:
            result.append(f"-{i}")
        else:
            result.append(i)
    return result


iterator = iter(iterator_func())
for _ in iterator_func():
    print(next(iterator))
