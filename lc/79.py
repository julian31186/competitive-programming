class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        vis = set()
        def dfs(i,j,idx):
            if not (i >= 0 and i < len(board) and j >= 0 and j < len(board[0])) or (i,j) in vis or word[idx] != board[i][j]: return False
            if idx == len(word) - 1: return True
            vis.add((i,j))
            w,x,y,z = dfs(i + 1,j,idx + 1), dfs(i - 1,j,idx + 1), dfs(i,j + 1,idx + 1), dfs(i,j - 1,idx + 1)
            vis.remove((i,j))
            return w or x or y or z


        res = False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    res |= dfs(i,j,0)
        
        return res