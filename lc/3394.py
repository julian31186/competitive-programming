class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        def ls(r):
            N = len(r)
            c = defaultdict(int)
            pre = defaultdict(int)
            curr = 0
            acc = 0
            first_break = 0
            for x1,_,x2,_ in r:
                c[(x1,0)] += 1
                c[(x2,1)] -= 1
            for x,t in sorted(c):
                if t == 1:
                    acc += abs(c[(x,t)])
                    pre[x] = acc
            for i,x in enumerate(sorted(set([x[0] for x in c.keys()]))):
                curr += c[(x,1)]
                if curr == 0 and first_break and (pre[x] - pre[first_break] > 0) and (N - pre[x] > 0):
                    return True
                if i != 0 and curr == 0 and first_break == 0:
                    first_break = x
                curr += c[(x,0)]
            return False
        return ls(rectangles) or ls([[y1,x1,y2,x2] for x1,y1,x2,y2 in rectangles])