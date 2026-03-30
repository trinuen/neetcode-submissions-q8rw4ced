class Solution:
    def trap(self, height: List[int]) -> int:
        total = 0
        for i in range(len(height)):
            l = i
            r = i
            #find highest left
            temp = i
            while temp >= 0:
                if height[l] <= height[temp]:
                    l = temp
                temp -= 1

            #find highest right
            temp = i
            while temp < len(height):
                if height[r] <= height[temp]:
                    r = temp
                temp += 1

            total += min(height[l], height[r]) - height[i]
        return total