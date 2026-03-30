class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        #area formula is (right - left + 1) * height

        stack = []
        max_area = 0

        for i in range(len(heights)):
            if not stack or heights[i] >= stack[-1][0]:
                stack.append([heights[i], i])

            else:
                while stack and heights[i] < stack[-1][0]:
                    nums = stack.pop()
                    max_area = max(max_area, (i - nums[1]) * nums[0])
                stack.append([heights[i], nums[1]])

        for i in range(len(stack)):
            max_area = max(max_area, (len(heights) - stack[i][1]) * stack[i][0])

        return max_area