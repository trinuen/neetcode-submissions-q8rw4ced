class MedianFinder:

    def __init__(self):
        self.smaller_vals = [] #max heap
        self.larger_vals = [] #min heap
        heapq.heapify(self.smaller_vals)
        heapq.heapify(self.larger_vals)

    def addNum(self, num: int) -> None:
        if not self.smaller_vals or num >= -self.smaller_vals[0]:
            heapq.heappush(self.larger_vals, num)
        else:
            heapq.heappush(self.smaller_vals, -num)
        
        if len(self.smaller_vals) - len(self.larger_vals) > 1:
            heapq.heappush(self.larger_vals, -heapq.heappop(self.smaller_vals))
        elif len(self.larger_vals) - len(self.smaller_vals) > 1:
            heapq.heappush(self.smaller_vals, -heapq.heappop(self.larger_vals))

    def findMedian(self) -> float:
        total_len = len(self.smaller_vals) + len(self.larger_vals) 
        if total_len % 2 == 0:
            return (-self.smaller_vals[0] + self.larger_vals[0])/2
        if len(self.smaller_vals) > len(self.larger_vals):
            return -self.smaller_vals[0]
        return self.larger_vals[0]
        