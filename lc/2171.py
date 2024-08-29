class Solution:
    def minimumRemoval(self, beans: List[int]) -> int:
        N,res = len(beans),inf
        beans.sort()
        pre,post = [0] * N,[0] * N
        for i in range(len(beans) - 1, -1, -1):
            post[i] = beans[i] + (post[i + 1] if i + 1 < len(beans) else 0)
        for i in range(len(beans)):
            pre[i] = beans[i] + (pre[i - 1] if i - 1 >= 0 else 0)
        for i in range(len(beans)):
            res = min(res,(pre[i - 1] if i - 1 >= 0 else 0) + (post[i + 1] - ((N - i - 1) * beans[i]) if i + 1 < len(beans) else 0))
        return res