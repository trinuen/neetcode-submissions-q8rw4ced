from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque([])
        res = []
        l = 0
        for r in range(len(nums)):
            while dq and nums[r] > nums[dq[-1]]:
                dq.pop()
            dq.append(r)

            if l > dq[0]: #this check if the max still in our window
                dq.popleft()
            
            if r + 1 >= k:
                res.append(nums[dq[0]])
                l += 1
        return res