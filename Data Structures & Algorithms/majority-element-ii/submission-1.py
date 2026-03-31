class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count1, res1 = 0, 0
        count2, res2 = 0, 0
        n = len(nums) // 3
        for num in nums:
            if count1 == 0:
                res1 = num
            elif count2 == 0:
                res2 = num
    
            if num != res1 and num != res2:
                count1 -= 1
                count2 -= 1
            elif num == res1:
                count1 += 1
            else:
                count2 += 1

        count1 = count2 = 0
        for num in nums:
            if num == res1:
                count1 += 1
            elif num == res2:
                count2 += 1

        if count1 > n and count2 > n:
            return [res1, res2]
        elif count1 > n:
            return [res1]
        elif count2 > n:
            return [res2]
        return []