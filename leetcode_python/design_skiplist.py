import random

MAX_LEVEL = 16
P = 5


class Skiplist:

    def __init__(self):
        self.head = Node(-1, MAX_LEVEL + 1)

    def search(self, target: int) -> bool:
        pos = self.__search_node(target)
        return pos.num == target

    def add(self, num: int) -> None:
        pos = self.__search_node(num)
        new = Node(num, self.__random_level())
        new.backward = pos
        for level in range(0, len(new.forward)):
            f = pos
            while f.backward is not None and len(f.forward) < level + 1:
                f = f.backward
            if level == 0 and f.forward[level] is not None:
                f.forward[level].backward = new
            new.forward[level] = f.forward[level]
            f.forward[level] = new

    def erase(self, num: int) -> bool:
        pos = self.__search_node(num)
        if pos.num != num:
            return False
        else:
            for level in range(0, len(pos.forward)):
                f = pos.backward
                while f.backward is not None and len(f.forward) < level + 1:
                    f = f.backward
                if level == 0 and f.forward[level].forward[level] is not None:
                    f.forward[level].forward[level].backward = f
                f.forward[level] = f.forward[level].forward[level]
            return True

    def __is_empty(self):
        return self.head.forward[0] is None

    def __search_node(self, num):
        if self.__is_empty():
            return self.head
        cur = self.head
        for index in range(MAX_LEVEL, -1, -1):
            while cur.forward[index] is not None and cur.forward[index].num <= num:
                cur = cur.forward[index]
        return cur

    def __random_level(self):
        level = 1
        while random.randint(0, 10) < P and level + 1 < MAX_LEVEL:
            level += 1
        return level


class Node:
    def __init__(self, num, level):
        self.backward = None
        self.forward = [None for _ in range(0, level)]
        self.num = num


if __name__ == '__main__':
    # Your Skiplist object will be instantiated and called as such:
    obj = Skiplist()
    param_1 = obj.search(10)
    obj.add(20)
    obj.search(20)
    param_3 = obj.erase(20)
