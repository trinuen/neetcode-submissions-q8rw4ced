import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        res = nums[0]
        heapq.heapify(nums)
        #[1,2,3,4,5]
        for i in range(len(nums) - k + 1):
            res = heapq.heappop(nums)
        return res