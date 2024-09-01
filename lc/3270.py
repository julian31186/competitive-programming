class Solution:
    def generateKey(self, n1: int, n2: int, n3: int) -> int:
        n1,n2,n3 = str(n1),str(n2),str(n3)
        n1 = n1.zfill(4)
        n2 = n2.zfill(4)
        n3 = n3.zfill(4)
        res = ""
        for i in range(len(n1)):
            res += str(min(int(n1[i]),int(n2[i]),int(n3[i])))
        return int(res)