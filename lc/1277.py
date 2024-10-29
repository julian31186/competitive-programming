class Solution:
    def countSquares(self, mat: List[List[int]]) -> int:
        res = 0

        def matrix_prefix(mat):
            for i in range(len(mat)):
                for j in range(len(mat[0])):
                    top = mat[i - 1][j] if i - 1 >= 0 else 0
                    left = mat[i][j - 1] if j - 1 >= 0 else 0
                    topleft = mat[i - 1][j - 1] if i - 1 >= 0 and j - 1 >= 0 else 0
                    mat[i][j] += top + left - topleft
            return
        
        matrix_prefix(mat)
        
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                for k in range(len(mat)):
                    if i - k >= 0 and j - k >= 0:
                        if (mat[i][j] - (mat[i - k - 1][j] if i - k - 1 >= 0 else 0) - (mat[i][j - k - 1] if j - k - 1 >= 0 else 0) + (mat[i - k - 1][j - k - 1] if i - k - 1 >= 0 and j - k - 1 >= 0 else 0)) == (k + 1) * (k + 1): res += 1
                    else:
                        break
        return res