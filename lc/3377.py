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

sieve = Sieve()

class Solution:
    def minOperations(self, n: int, m: int) -> int:
        #djik with banned states (1000th) problem)
        h = [(n,str(n))]
        dists = defaultdict(lambda: inf)
        dists[n] = n
        while h:
            cost,num = heappop(h)
            if dists[int(num)] < cost or sieve.is_prime(int(num)):
                continue
            if int(num) == m: return cost
            for i,c in enumerate(num):

                if c != '9':
                    nxt = str(int(c) + 1)
                    new = num[:i] + nxt + num[i + 1:]
                    if cost + int(new) < dists[int(new)]:
                        dists[int(new)] = cost + int(new)
                        heappush(h,(cost + int(new), new))
                if c != '0':
                    nxt = str(int(c) - 1)
                    new = num[:i] + nxt + num[i + 1:]
                    if new[0] == '0': continue
                    if cost + int(new) < dists[int(new)]:
                        dists[int(new)] = cost + int(new)
                        heappush(h,(cost + int(new), new))

        return -1
        