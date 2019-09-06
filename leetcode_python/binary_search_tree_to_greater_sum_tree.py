class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    gst = 0

    def bstToGst(self, root: TreeNode) -> TreeNode:
        self.gst = 0
        self.__dfs(root)
        return root


    def __dfs(self, root: TreeNode):
        if root is None:
            return
        self.__dfs(root.right)
        root.val = root.val + self.gst
        self.gst = root.val
        self.__dfs(root.left)
