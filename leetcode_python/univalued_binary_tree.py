# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    uni_value = None

    def isUnivalTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return False
        else:
            self.uni_value = root.val
            return self.isUnivalTreeInternal(root.left) and self.isUnivalTreeInternal(root.right)

    def isUnivalTreeInternal(self, root):
        """
        :param root: TreeNode
        :return: bool
        """
        if root is None:
            return True
        else:
            return self.isUnivalTreeInternal(root.left) and self.isUnivalTreeInternal(root.right) and root.val == self.uni_value

