# Ikkita sonni qo'shadigan funksiyaga dekorator qo'shing, bunda
# funksiya qiymati 2 ga ko'payirilgan holda qaytarilsin.
# add(2, 3)  # 10
# add(5, 5)  # 20
def add_func(num, num_2):
    def func():
        return (num + num_2) * 2

    return func


result = add_func(5, 5)
print(result())
