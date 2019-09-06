import random

class RandomizedSet:
    def __init__(self):
        self.set = set()
        """
        Initialize your data structure here.
        """

    def insert(self, val: int) -> bool:
        if val in self.set:
            return False
        else:
            self.set.add(val)
            return True

    def remove(self, val: int) -> bool:
        if val in self.set:
            self.set.remove(val)
            return True
        else:
            return False

    def getRandom(self) -> int:
        if not self.set:
            return None
        return random.choice(list(self.set))
