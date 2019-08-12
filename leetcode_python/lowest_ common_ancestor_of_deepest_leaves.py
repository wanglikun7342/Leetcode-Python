class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    result = None
    max_depth = 0

    def lcaDeepestLeaves(self, root: TreeNode) -> TreeNode:
        self.__dfs(root, 0)
        return self.result


    def __dfs(self, root, depth):
        if root is None:
            return depth - 1
        left = self.__dfs(root.left, depth + 1)
        right = self.__dfs(root.right, depth + 1)
        if right == left and right >= self.max_depth:
            self.result = root
            self.max_depth = right
        if left > right:
            return left
        else:
            return right
