class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        #len(matrix)
        #len(matrix[0])

        l = 0
        r = len(matrix) - 1
        n = len(matrix[0]) - 1

        while l <= r:
            mid = (l + r)//2
            if matrix[mid][-1] == target:
                return True
            elif matrix[mid][-1] < target:
                l = mid + 1
            else:
                l2 = 0
                r2 = n
                while l2 <= r2:
                    mid2 = (l2 + r2)//2
                    if matrix[mid][mid2] == target:
                        return True
                    elif matrix[mid][mid2] < target:
                        l2 = mid2 + 1
                    else:
                        r2 = mid2 - 1
                r = mid - 1

        return False
        

                
                
