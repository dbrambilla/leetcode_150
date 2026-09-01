from typing import List, Dict, Tuple
class TimeMap:
    cache: Dict[str, List[Tuple[str, int]]]

    def __init__(self):       
        self.cache = dict()

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.cache:
            self.cache[key] = []
        self.cache[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        def search(elements: List[Tuple[str, int]], ts: int) -> str:
            l: int = 0
            r: int = len(elements) - 1
            res: str = ""
            while l <= r:
                m: int = l + (r - l) // 2
                if elements[m][1] == ts:
                    return elements[m][0]
                
                if elements[m][1] < ts:
                    res = elements[m][0]
                    l = m + 1
                else:
                    r = m - 1

            return res

        if key not in self.cache:
            return ""
        
        return search(self.cache[key], timestamp)

# ["TimeMap", 
# "set", ["test", "one", 10], 
# "set", ["test", "two", 20], 
# "set", ["test", "three", 30], 
# "get", ["test", 15], 
# "get", ["test", 25], 
# "get", ["test", 35]]
timeMap: TimeMap = TimeMap();
print(timeMap.set("key1", "one", 10))
print(timeMap.set("key1", "two", 20))
print(timeMap.set("key1", "three", 30))
print(timeMap.get("key1", 15))
print(timeMap.get("key1", 25))         
print(timeMap.get("key1", 35))  

timeMap: TimeMap = TimeMap();
print(timeMap.set("alice", "happy", 1))
print(timeMap.get("alice", 1))
print(timeMap.get("alice", 2))         
print(timeMap.set("alice", "sad", 3))
print(timeMap.get("alice", 3))  

# ["TimeMap", "set", ["key1", "value1", 10], "get", ["key1", 1], "get", ["key1", 10], "get", ["key1", 11]]
timeMap: TimeMap = TimeMap();
print(timeMap.set("key1", "value1", 10))
print(timeMap.get("key1", 1))
print(timeMap.get("key1", 10))         
print(timeMap.get("key1", 11))                
