# only_even_parameters nomli dekorator yarating, bunda quyidagi funksiyallarda
# ishlating va tegishli natija qaytaring.
def only_even_parameters(func):
    def divide_inner(*args):
        for i in args:
            if i % 2 == 0:
                return func(*args)
            else:
                return 'Please add only even numbers!'

    return divide_inner


@only_even_parameters
def add(a, b):
    return a + b


print(add(6, 8))  # 14
print(add(1, 4))  # Please add only even numbers!


@only_even_parameters
def multiply(a, b, c, d):
    return a * b * c * d


print(multiply(2, 3, 4, 2))
print(multiply(3, 3, 4, 2))
