class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count1, res1 = 0, 0
        count2, res2 = 0, 0
        n = len(nums) // 3
        for num in nums:
            if num == res1:
                count1 += 1
            elif num == res2:
                count2 += 1
            elif count1 == 0:
                res1 = num
                count1 = 1
            elif count2 == 0:
                res2 = num
                count2 = 1
            else:
                count1 -= 1
                count2 -= 1


        count1 = count2 = 0
        for num in nums:
            if num == res1:
                count1 += 1
            elif num == res2:
                count2 += 1
        res = []
        if count1 > n:
            res.append(res1)
        if count2 > n:
            res.append(res2)
        return res