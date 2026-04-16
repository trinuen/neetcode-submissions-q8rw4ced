class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        ROWS = len(matrix)
        COLS = len(matrix[0])

        self.sum_mat = [[0] * (COLS+1) for _ in range(ROWS+1)]
        for i in range(1, ROWS+1):
            pre = 0
            for j in range(1, COLS+1):
                self.sum_mat[i][j] += matrix[i-1][j-1]
                self.sum_mat[i][j] += pre
                self.sum_mat[i][j] += self.sum_mat[i-1][j]
                pre += matrix[i-1][j-1]


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.sum_mat[row2+1][col2+1] - self.sum_mat[row2+1][col1] - self.sum_mat[row1][col2+1] + self.sum_mat[row1][col1]
#(1,1,1,2)
#[[0,0,0,0,0,0]
# [0,3,3,4,7,9],
# [0,8,14,18,2,1],
# [0,1,2,0,1,5],
# [0,4,1,0,1,7],
# [0,1,0,3,0,5]]
# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)