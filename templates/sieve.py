'''
Used to generate all prime numbers in the range [2,N] (inclusive) (sorted aka can bin search it if needed)
Pass N into constructor and access list of primes with .primes attribute

first_n_primes(n)
- Returns the first n primes up to N passed into Sieve constructor if there are n primes
- Returns [] if there are NOT n primes that exist in the range [2,N]

get_primes()
- Returns list of primes between [2,N]

is_prime(n)
- Checks if n is a prime number in O(1) (If n is within the range [0,N]) 

TC: O(n * log log n)
SC: O(N)
'''
from math import isqrt

class Sieve():
    def __init__(self,N=10**7):
        self.is_p = [True] * (N + 1)
        self.is_p[0] = False
        self.is_p[1] = False
        self.primes = self._sieve(N + 1)
        
    def _sieve(self,N):
        for i in range(isqrt(N - 1) + 1):
            if i >= 2 and self.is_p[i]:
                for j in range(i**2,N,i):
                    self.is_p[j] = False
        return [n for n in range(N) if self.is_p[n]]

    def get_primes(self):
        return self.primes

    def is_prime(self,n):
        return self.is_p[n]

    def first_n_primes(self,n):
        return self.primes[:n] if len(self.primes) >= n else []