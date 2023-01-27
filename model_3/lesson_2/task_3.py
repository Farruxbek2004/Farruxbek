# Ikkita sonni qo'shadigan funksiyaga dekorator qo'shing, bunda
# funksiya qiymati 2 ga ko'payirilgan holda qaytarilsin.
# add(2, 3)  # 10
# add(5, 5)  # 20
def add_func(func):
    def add_result_func(number, number_2):
        return func(number, number_2) * 2

    return add_result_func


@add_func
def value(number, number_2):
    return number + number_2


result = value(5, 3)
print(result)
