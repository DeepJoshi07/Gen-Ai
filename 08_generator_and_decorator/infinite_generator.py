def increment():
    count = 1
    while(True):
        yield count
        count += 5

number = increment()

for _ in range(10):
    print(next(number))