class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        max_water = 0
        r = len(heights) - 1
        l = 0

        while (r > l):
            water = (r - l) * min(heights[l], heights[r])
            max_water = max(water, max_water)
            if heights[l] >= heights[r]:
                r -= 1
            else:
                l += 1

        return max_water