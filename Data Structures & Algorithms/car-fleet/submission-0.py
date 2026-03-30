class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        pairs = sorted(zip(position, speed))[::-1]
        print(pairs)
        stack = []

        for pair in pairs:
            #calculate time
            time = (target - pair[0]) / pair[1]
            if not stack:
                stack.append(pair)
            else:
                if time > ((target - stack[-1][0]) / stack[-1][1]):
                    stack.append(pair)

        return len(stack)