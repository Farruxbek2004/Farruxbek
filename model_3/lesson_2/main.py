# my_list = list(range(2,21,2))
# iterator = iter(my_list)
# for _ in my_list:
#     print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator,''))

# def generator():
#     yield 1
#     yield 2
#     yield 3


# def get_generator(number):
#     for i in number:
#         yield i * i
#
#
# number = [1, 2, 3, 4, 5, 6]
# result = get_generator(number)
# print(next(result))
# print(next(result))
# print(next(result))
# print(next(result))
# print(next(result))
# print(next(result))
# print(next(result, 'Error'))
# def hello(name):
#     # ichki funksiya
#     def get_name():
#         return f"Hello, {name}!"
#
#     # icki funksiyani qaytarish
#     return get_name
#
#
# hello_func = hello("Sarvar")
# print(hello_func())  # Hello, Sarvar!

# def divide_decorator(func):
#     def divide_inner(a, b):
#         try:
#             return func(a, b)
#         except ZeroDivisionError:
#             raise "Nolga bo'lish mumkin emas!"
#
#     return divide_inner
#
#
# def increment_arg_if_second_zero(func):
#     def inner(a, b):
#         if b == 0:
#             b += 1
#         return func(a, b)
#
#     return inner
#
# @divide_decorator
# @increment_arg_if_second_zero
# def divider(a, b):
#     return a / b
#
#
# print(divider(10, 5))  # 2.0
# print(divider(10, 0))  # 10.0
