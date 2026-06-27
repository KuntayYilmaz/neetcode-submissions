class TimeMap:

    def __init__(self):
        self.hashmap = {}
 
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.hashmap:
            self.hashmap[key] = []
        self.hashmap[key].append([timestamp,value])


    def get(self, key: str, timestamp: int) -> str:
        if key not in self.hashmap:
            return ""
        l, r = 0, len(self.hashmap[key]) - 1
        res = ""
        while l <= r:
            mid = (l + r) // 2
            curr = self.hashmap[key][mid][0]
            if curr <= timestamp:
                res = self.hashmap[key][mid][1]
                l = mid + 1
            else:
                r = mid - 1

        return res

        
