

#### generate a set containing prime numbers from 2 to n ####
def prime_sieve(n):
    primes = set(range(2, n+1))
    for i in range(2, (n+1) // 2):
        if i in primes:
            m = 2
            while i*m <= n:
                primes.discard(i*m)
                m += 1
    return primes

#### this is not a good algorithm to check prime numbers ####
def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


