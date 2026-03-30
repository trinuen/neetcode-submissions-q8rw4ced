class TimeMap:

    def __init__(self):
        self.timemap = {}

        #{"alice": [("happy", 3), ("sad", 4), ("angry", 5)]}
        #if the time we looking for does not exist
        # we want to return the right pointer after binary search failed
        #return left pointer if time is less than the min time
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.timemap:
            self.timemap[key].append((value, timestamp))
        else:
            self.timemap[key] = [(value, timestamp)]

    def get(self, key: str, timestamp: int) -> str:
        if key in self.timemap and timestamp >= self.timemap[key][0][1]:
            log = self.timemap[key]
            l = 0
            r = len(log) - 1
            while l <= r:
                m = (l + r) // 2
                if log[m][1] == timestamp:
                    return log[m][0]
                elif log[m][1] <= timestamp:
                    l = m + 1
                else:
                    r = m - 1

            return log[r][0]

        return ""