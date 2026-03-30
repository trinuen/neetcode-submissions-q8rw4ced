class Solution:
    def trap(self, height: List[int]) -> int:
        total = 0
        prefix = [1] * len(height)
        suffix = [1] * len(height)

        highest = 0
        for i in range(len(height)):
            prefix[i] = max(height[i], height[highest])
            if height[i] > height[highest]:
                highest = i
        
        highest = len(height)-1
        for j in range(len(height)-1, -1, -1):
            suffix[j] = max(height[j], height[highest])
            if height[j] > height[highest]:
                highest = j
        
        for i in range(len(height)):
            total += min(prefix[i], suffix[i]) - height[i]
        return total