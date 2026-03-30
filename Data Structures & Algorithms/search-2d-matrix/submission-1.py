class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        l = 0
        r = len(matrix) - 1

        while l <= r:
            mid = (l + r)//2
            if target <= matrix[mid][-1] and target >= matrix[mid][0]:
                break
            elif target > matrix[mid][-1]:
                l = mid + 1
            else:
                r = mid - 1

        l = 0
        r = len(matrix[0]) - 1
        while l <= r:
            mid2 = (l + r)//2
            if target == matrix[mid][mid2]:
                return True
            elif target > matrix[mid][mid2]:
                l = mid2 + 1
            else:
                r = mid2 - 1

        return False