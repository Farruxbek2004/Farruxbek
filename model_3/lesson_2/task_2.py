# get_next_prime generator funksiya yarating, bunda 1 dan 1000 gacha sonlar orasida tub
# sonlarni next() orqali olish mumkin bo'lsin.
# prime_generator = get_next_prime()
# print(next(prime_generator))  # 2
# print(next(prime_generator))  # 3
# print(next(prime_generator))  # 5
def get_next_prime():
    for i in range(2, 1000):
        for j in range(2, i):

            if i % j == 0:
                break

        else:
            yield i


generator = get_next_prime()

for _ in range(10):
    print(next(generator))
