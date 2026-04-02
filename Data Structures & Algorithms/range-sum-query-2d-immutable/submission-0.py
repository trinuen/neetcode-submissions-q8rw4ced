class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        ROWS = len(matrix)
        COLS = len(matrix[0])
        self.sum_matrix = [[0] * (COLS + 1) for _ in range(ROWS + 1)]

        for i in range(ROWS):
            prefix = 0
            for j in range(COLS):
                prefix += matrix[i][j]
                above = self.sum_matrix[i][j+1]
                self.sum_matrix[i+1][j+1] = prefix + above


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row1 += 1
        col1 += 1
        row2 += 1
        col2 += 1
        mat = self.sum_matrix
        return mat[row2][col2] - mat[row2][col1-1] - mat[row1-1][col2] + mat[row1-1][col1-1]
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)