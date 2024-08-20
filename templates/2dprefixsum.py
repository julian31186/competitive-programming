
'''

Returns the 2D prefix sum on a matrix (modifies the reference)

1 2 3      1  3  6
4 5 6  --> 5  12 21
7 8 9      12 27 45

1 2     1 3
3 4 --> 4 10
5 6     9 21

1 2 3 --> 1  3  6
4 5 6     5  12 21

'''

def matrix_prefix(mat):
    
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            top = mat[i - 1][j] if i - 1 >= 0 else 0
            left = mat[i][j - 1] if j - 1 >= 0 else 0
            topleft = mat[i - 1][j - 1] if i - 1 >= 0 and j - 1 >= 0 else 0
            mat[i][j] += top + left - topleft
    return
