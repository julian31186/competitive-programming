class Solution:
    def reportSpam(self, message: List[str], bannedWords: List[str]) -> bool:
        s = set(bannedWords)
        cnt = 0
        for i in range(len(message)):
            if message[i] in s: cnt += 1
        return cnt >= 2