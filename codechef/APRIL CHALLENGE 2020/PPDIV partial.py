# IMPORTS
import collections
import itertools
# END OF IMPORTS

# HELPER FUNCTIONS
def prime_factors(n):
    i = 2
    while i * i <= n:
        if n % i == 0:
            n /= i
            yield i
        else:
            i += 1

    if n > 1:
        yield n
def prod(iterable):
    result = 1
    for i in iterable:
        result *= i
    return result
def get_divisors(n):
    pf = prime_factors(n)

    pf_with_multiplicity = collections.Counter(pf)

    powers = [
        [factor ** i for i in range(count + 1)]
        for factor, count in pf_with_multiplicity.items()
    ]

    for prime_power_combo in itertools.product(*powers):
        yield prod(prime_power_combo)
def primes(n): # sieve of eratosthenes
    i, p, ps, m = 0, 3, [2], n // 2
    sieve = [True] * m
    while p <= n:
        if sieve[i]:
            ps.append(p)
            for j in range(int((p*p-3)/2), m, p):
                sieve[j] = False
        i, p = i+1, p+2
    return ps
def iroot(k, n): # assume n > 0
    u, s, k1 = n, n+1, k-1
    while u < s:
        s = u
        u = (k1 * u + n // u ** k1) // k
    return s
def ilog(b, n): # max e where b**e <= n
    lo, blo, hi, bhi = 0, 1, 1, b
    while bhi < n:
        lo, blo, hi, bhi = hi, bhi, hi+hi, bhi*bhi
    while 1 < (hi - lo):
        mid = (lo + hi) // 2
        bmid = blo * pow(b, (mid - lo))
        if n < bmid: hi, bhi = mid, bmid
        elif bmid < n: lo, blo = mid, bmid
        else: return mid
    if bhi == n: return hi
    return lo
def isPerfectPower(n): # x if n == x ** y, or False
    for p in primes(ilog(2,n)):
        x = iroot(p, n)
        if pow(x, p) == n: return x
    return False       
# END OF FUNCTIONS

# SOLUTION
for _ in range(int(input())):
    n = int(input())
    sum_upto_n = 0
    for i in range(1,n+1):
        sum_upto_n += sum([j for j in get_divisors(i) if isPerfectPower(j)])
    print(int(sum_upto_n))
    