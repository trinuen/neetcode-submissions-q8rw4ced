class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        res = [0] * len(temperatures)
        stack = [] #(index, temperatures[index])

        for i in range(len(temperatures)):
            while stack and temperatures[i] > stack[-1][1]:
                stackInd, stackVal = stack.pop()
                res[stackInd] = i - stackInd
            stack.append([i, temperatures[i]])
        return res