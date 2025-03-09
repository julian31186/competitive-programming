class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        res = len(fruits)
        vis = set()
        for f in fruits:
            for i,b in enumerate(baskets):
                if i not in vis and b >= f:
                    vis.add(i)
                    res -= 1
                    break
        return res