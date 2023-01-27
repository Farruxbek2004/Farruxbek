def generate_ints(number):
    yield number
    yield number + number
    yield number + number + number
    yield number + number + number + number
    yield number + number + number + number + number


gen = generate_ints(3)
res = iter(gen)
while True:
    try:
        print(next(res))
    except StopIteration:
        break
