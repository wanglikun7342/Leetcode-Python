from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        if preorder is None or len(preorder) == 0:
            return None
        else:
            root = TreeNode(preorder[0])
            for value in preorder[1:]:
                self.__build(root, value)
            return root

    def __build(self, root, value):
        if value > root.val:
            if root.right is not None:
                self.__build(root.right, value)
            else:
                root.right = TreeNode(value)
        elif value < root.val:
            if root.left is not None:
                self.__build(root.left, value)
            else:
                root.left = TreeNode(value)


if __name__ == '__main__':
    input_array = [8, 5, 1, 7, 10, 12]
    solution = Solution()
    solution.bstFromPreorder(input_array)
