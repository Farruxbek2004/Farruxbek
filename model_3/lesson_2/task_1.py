def generate_ints(number):
    value = number
    while True:
        yield number
        number += value


gen = generate_ints(3)
res = iter(gen)
for _ in range(5):
    print(next(res))
