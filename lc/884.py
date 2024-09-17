class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        x,y,res = {},{},[]
        for w in s1.split(" "):
            if w not in x: x[w] = 1
            else: x[w] += 1
        for w in s2.split(" "):
            if w not in y: y[w] = 1
            else: y[w] += 1
        for w in x:
            if x[w] == 1 and w not in y: res.append(w)
        for w in y:
            if y[w] == 1 and w not in x: res.append(w)
        return res