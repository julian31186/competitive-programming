class Solution:
    def stringHash(self, s: str, k: int) -> str:
        arr = []
        res = ""
        for i in range(0,len(s), k):
            arr.append(list(s[i : i + k]))
        for i in range(len(arr)):
            acc = 0
            for j in range(len(arr[i])):
                acc += ord(arr[i][j]) - ord('a')
            acc %= 26
            res += chr(acc + ord('a')) 
        return res