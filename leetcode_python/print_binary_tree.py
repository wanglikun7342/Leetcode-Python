from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def printTree(self, root: TreeNode) -> List[List[str]]:
        depth = self.__dfs(root)
        result = [["" for _ in range(pow(2, depth) - 1)] for _ in range(depth)]
        self.__print(result, root, 0, 0, (len(result[0]) - 1) // 2)
        return result

    def __print(self, result, root: TreeNode, base, level, offset):
        if root is None:
            return
        new = base + offset
        result[level][new] = str(root.val)
        self.__print(result, root.left, new, level + 1, -((abs(new - base) - 1) // 2 + 1))
        self.__print(result, root.right, new, level + 1, (abs(new - base) - 1) // 2 + 1)

    def __dfs(self, root: TreeNode):
        if root is None:
            return 0
        return max(self.__dfs(root.left) + 1, self.__dfs(root.right) + 1)

if __name__ == '__main__':
    root = TreeNode(1)
    solution = Solution()
    solution.printTree(root)
