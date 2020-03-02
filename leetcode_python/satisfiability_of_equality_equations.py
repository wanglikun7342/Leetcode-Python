from typing import List


class Solution:
    def __init__(self):
        self.parent = [i for i in range(26)]

    def __find(self, x):
        while x != self.parent[x]:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def __union(self, x, y):
        root_x = self.__find(x)
        root_y = self.__find(y)
        self.parent[root_x] = root_y

    def equationsPossible(self, equations: List[str]) -> bool:
        for equation in equations:
            if equation[1] == '=':
                self.__union(ord(equation[0]) - ord('a'), ord(equation[3]) - ord('a'))
        for equation in equations:
            if equation[1] == '!':
                if self.__find(ord(equation[0]) - ord('a')) == self.__find(ord(equation[3]) - ord('a')):
                    return False
        return True

if __name__ == '__main__':
    equations = ["a==b","b==a"]
    solution = Solution()
    print(solution.equationsPossible(equations))
