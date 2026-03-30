class Solution:
    def trap(self, height: List[int]) -> int:  
        total = 0
        l = 0
        r = len(height) - 1

        max_l, max_r = height[l], height[r]

        while r >= l:
            if max_r >= max_l:
                
                max_l = max(max_l, height[l])
                total += max_l - height[l]
                l += 1
                
            else:
                
                max_r = max(max_r, height[r])
                total += max_r - height[r]
                r -= 1
            
        return total