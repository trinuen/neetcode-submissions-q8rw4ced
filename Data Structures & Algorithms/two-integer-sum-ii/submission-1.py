class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        i = 0
        j = len(numbers) - 1

        while (True):
            if numbers[j] + numbers[i] > target:
                j = j - 1
            elif numbers[j] + numbers[i] < target:
                i = i + 1
            else:
                return [i+1,j+1]
            