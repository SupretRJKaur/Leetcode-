import collections

class TimeMap(object):

    def __init__(self):
        self.store = collections.defaultdict(list)

    def set(self, key, value, timestamp):
        self.store[key].append([timestamp, value])

    def get(self, key, timestamp):
        res = ""
        values = self.store.get(key, [])
        
        i = 0
        j = len(values) - 1
        
        while i <= j:
            mid = (i + j) // 2
            if values[mid][0] <= timestamp:
                res = values[mid][1]
                i = mid + 1
            else:
                j = mid - 1
                
        return res
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)