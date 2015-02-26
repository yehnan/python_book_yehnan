

# from itertools import imap as map
from itertools import repeat, chain

def prime_sieve(n):
    primes = set(range(2, n+1))
    for i in range(2, (n+1+1) // 2):
        if i in primes:
            m = 2
            while i*m <= n:
                primes.discard(i*m)
                m += 1
    return primes

def gen_pairs(i):
    return map(lambda i,j: (i,j), repeat(i), range(1, i))

def gen_allpairs(n):
    return chain(*map(gen_pairs, range(2, n+1)))

def pair_sum(p):
    return (p[0], p[1], p[0]+p[1])

def is_prime(ps):
    return ps[2] in prime_sieve(ps[2])

def sum_is_prime(n):
    return filter(is_prime, map(pair_sum, gen_allpairs(n)))

print(list(sum_is_prime(6)))



