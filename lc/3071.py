class Solution:
    def minimumOperationsToWriteY(self, grid: List[List[int]]) -> int:
        res,y,not_y,y_set,n,mid = inf,defaultdict(int),defaultdict(int),set(),len(grid),len(grid) // 2
        def valid(i,j):
            return i >= 0 and j >= 0 and i < len(grid) and j < len(grid[0])
        
        def go(i,j,i_dir,j_dir):
            while valid(i,j):
                y[grid[i][j]] += 1
                y_set.add((i,j))
                i += i_dir
                j += j_dir
        
        go(mid,mid,1,0)
        go(mid - 1, mid - 1, -1, -1)
        go(mid - 1, mid + 1, -1, 1)
        
        for i in range(n):
            for j in range(n):
                if (i,j) not in y_set:
                    not_y[grid[i][j]] += 1
        
        ty,tny = sum(y.values()),sum(not_y.values())
        for in_y in [0,1,2]:
            for not_in_y in [0,1,2]:
                if in_y != not_in_y:
                    res = min(res, (ty - y[in_y]) + (tny - not_y[not_in_y]))
        return res