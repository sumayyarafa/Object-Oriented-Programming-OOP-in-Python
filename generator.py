def is_prime(number):
    if number < 2:
        return False 
    if number == 2:
        return True
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

def infinite_twin_primes():
    i = 3
    while True:
        if is_prime(i) and is_prime(i+2):
            yield (i, i+2)
        i += 1

gen = infinite_twin_primes()
for i in range(100):
    print(next(gen))