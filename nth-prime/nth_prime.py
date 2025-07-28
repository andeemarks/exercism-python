from functools import cache

def prime(number):
    if (number == 0):
        raise ValueError("there is no zeroth prime")
    
    primes = generate_n_primes(number)

    return primes[number - 1]

def generate_n_primes(number: int) -> list[int]:
    primes = []
    i = 2
    while (len(primes) < number):
        if is_prime(i):
            primes.append(i)

        i += 1

    return primes

@cache
def is_prime(n: int) -> bool:
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            return False

    return True
