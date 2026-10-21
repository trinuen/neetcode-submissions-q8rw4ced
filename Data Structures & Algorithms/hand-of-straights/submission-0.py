class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False
        count = {}
        for n in hand:
            count[n] = count.get(n,0) + 1
        
        minH = list(count.keys())
        heapq.heapify(minH)
        while minH:
            minVal = minH[0]
            for i in range(minVal, minVal + groupSize):
                if i not in count:
                    return False
                count[i] -= 1
                if count[i] == 0:
                    if i != minH[0]:
                        return False
                    heapq.heappop(minH)
        return True
        