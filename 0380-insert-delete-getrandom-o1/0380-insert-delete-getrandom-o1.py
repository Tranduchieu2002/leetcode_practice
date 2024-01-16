import numpy as np

class RandomizedSet:

    def __init__(self):
        self.record = []
        self.freq = defaultdict(int)

    def insert(self, val: int) -> bool:
        if val in self.freq:
            return False
        
        self.record.append(val)
        self.freq[val] += 1
        return True
        

    def remove(self, val: int) -> bool:
        if val not in self.freq:
            return False
        self.record.remove(val)
        
        self.freq[val] -= 1
        if self.freq[val] == 0:
            del self.freq[val]

        return True

    def getRandom(self) -> int:
        if(not self.record):
            return 
        return self.record[np.random.randint(len(self.record))]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()