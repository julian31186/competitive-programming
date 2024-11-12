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

p = Sieve(1000).primes

class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:
        def bins(i):
            l,r,x = 0,len(p) - 1,0
            while l <= r:
                mid = (r + l) // 2
                if i - 1 >= 0:
                    if nums[i] - p[mid] > nums[i - 1] and nums[i] - p[mid] > 0:    
                        x = p[mid]
                        l = mid + 1
                    else:
                        r = mid -1
                else:
                    if nums[i] - p[mid] > 0:
                        x = p[mid]
                        l = mid + 1
                    else:
                        r = mid -1
            return x

        nums[0] -= bins(0)
        for i in range(1,len(nums)):
            x = bins(i)
            if x == 0 and nums[i] <= nums[i - 1]: return False
            nums[i] -= x
        return True