

#
def prime_gf():
    primes = [2]
    def is_prime(n):
        for i in primes:
            if n % i == 0:
                return False
        return True
    while True:
        p = primes[-1]
        yield p
        while True:
            p += 1
            if is_prime(p):
                primes.append(p)
                break
prime_f = prime_gf()



