

from itertools import imap as map

def prime_sieve(n):
    primes = set(range(2, n+1))
    for i in range(2, (n+1+1) // 2):
        if i in primes:
            m = 2
            while i*m <= n:
                primes.discard(i*m)
                m += 1
    return primes

def is_prime(n):
    return n in prime_sieve(n)
def sum_of_primes(n):
    return sum(filter(is_prime, range(2, n+1)))

print(sum_of_primes(20))
print(sum_of_primes(2 * 1000))
