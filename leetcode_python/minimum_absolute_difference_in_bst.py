import sys


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        node_list = []
        self.__dfs(root, node_list)
        min_diff = sys.maxsize
        for index in range(1, len(node_list)):
            diff = node_list[index].val - node_list[index - 1].val
            if diff < min_diff:
                min_diff = diff
        return min_diff

    def __dfs(self, root, node_list):
        if root is None:
            return
        else:
            self.__dfs(root.left, node_list)
            node_list.append(root)
            self.__dfs(root.right, node_list)
