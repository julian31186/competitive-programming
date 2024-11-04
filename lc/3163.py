class Solution:
    def compressedString(self, word: str) -> str:
        word += "."
        res,cnt,prev = [],0,word[0]
        for r in range(len(word)):
            if word[r] != prev or cnt == 9:
                res.append(str(cnt))
                res.append(prev)
                prev,cnt = word[r],1
            else:
                cnt += 1
        return "".join(res)