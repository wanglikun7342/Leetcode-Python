# Definition for a binary tree node.
class TreeNode:

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        left_leafs = self.get_leafs(root1)
        right_leafs = self.get_leafs(root2)

        if len(left_leafs) != len(right_leafs):
            return False
        for index in range(len(left_leafs)):
            if left_leafs[index].val != right_leafs[index].val:
                return False

        return True

    def get_leafs(self, root: TreeNode) -> []:
        if root is None:
            return []
        leafs = []
        self.traverse_leafs(root, leafs)
        return leafs

    def traverse_leafs(self, root: TreeNode, leafs):
        if root is None:
            return
        if root.left is not None:
            self.traverse_leafs(root.left, leafs)
        if root.right is not None:
            self.traverse_leafs(root.right, leafs)
        if root.left is None and root.right is None:
            leafs.append(root)


if __name__ == '__main__':
    node1 = TreeNode(3)
    node2 = TreeNode(4)
    node1.left = node2
    solution = Solution()
    print(solution.leafSimilar(node1, node2))
