class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    diff = 100
    pre = -100
    def minDiffInBST(self, root: TreeNode) -> int:
        if root is None:
            return -100
        self.minDiffInBST(root.left)
        self.diff = min(self.diff, root.val - self.pre)
        self.pre = root.val
        self.minDiffInBST(root.right)
        return self.diff
