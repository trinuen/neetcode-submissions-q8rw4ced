import random
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        self.quickSort(nums, 0, len(nums) - 1)
        return nums
    def quickSort(self, nums, l, r):
        if r <= l:
            return

        pivot = self.partition(nums, l, r)
        self.quickSort(nums, l, pivot - 1)
        self.quickSort(nums, pivot + 1, r)
        
    def partition(self, nums, l, r):
        i = l - 1
        pivot_idx = random.randint(l, r)
        nums[pivot_idx], nums[r] = nums[r], nums[pivot_idx]

        pivot = nums[r]
        for j in range(l, r):
            if nums[j] < pivot:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]
        i +=1
        nums[i], nums[r] = nums[r], nums[i]
        return i