'''
Used to generate all prime numbers in the range [2,N] (inclusive) (sorted aka can bin search it if needed)
Pass N into constructor and access list of primes with .primes attribute

first_n_primes(n)
- Returns the first n primes up to N passed into Sieve constructor if there are n primes
- Returns [] if there are NOT n primes that exist in the range [2,N]


TC: O(n * log log n)
SC: O(N)
'''
from math import isqrt

class Sieve():
    def __init__(self,N=10**7):
        self.primes = self._sieve(N + 1)

    def _sieve(self,N):
        is_p = [True] * N
        is_p[0] = False
        is_p[1] = False
        
        for i in range(isqrt(N - 1) + 1):
            if i >= 2 and is_p[i]:
                for j in range(i**2,N,i):
                    is_p[j] = False
        return [n for n in range(N) if is_p[n]]

    def first_n_primes(self,n):
        return self.primes[:n] if len(self.primes) >= n else []