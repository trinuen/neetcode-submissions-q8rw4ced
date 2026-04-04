import random
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        return self.mergeSort(nums)
        
    def mergeSort(self, nums):
        if len(nums) <= 1:
            return nums
    
        mid = len(nums) // 2

        left_nums = self.mergeSort(nums[0:mid])
        right_nums = self.mergeSort(nums[mid:len(nums)])

        return self.merge(left_nums, right_nums)

    def merge(self, nums1, nums2):
        res = []
        i = j = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] >= nums2[j]:
                res.append(nums2[j])
                j += 1
            elif nums1[i] < nums2[j]:
                res.append(nums1[i])
                i += 1
            
        while i < len(nums1):
            res.append(nums1[i])
            i += 1
        while j < len(nums2):
            res.append(nums2[j])
            j += 1

        return res