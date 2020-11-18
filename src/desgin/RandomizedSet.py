import random


class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = dict()
        self.total = 0
        self.rand = random.Random()

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.data:
            return False
        self.data[val] = None
        self.total += 1
        return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val in self.data:
            self.data.pop(val)
            self.total -= 1
            return True
        return False

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        # 此处可以优化
        datas = list(self.data.keys())
        pos = self.rand.randint(0, len(datas) - 1)
        val = datas[pos]
        return val


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
# obj = RandomizedSet()
# param_1 = obj.insert(1)
# param_2 = obj.remove(2)
# param_3 = obj.getRandom()
# print(param_3)
obj = RandomizedSet()
obj.insert(1)
obj.insert(10)
obj.insert(20)
obj.insert(30)
a = []
for i in range(10000):
    a.append(obj.getRandom())

from collections import Counter

counter = Counter(a)
print(counter)
