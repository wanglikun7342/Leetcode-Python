# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        node_list = []
        while head is not None:
            node_list.append(head.val)
            head = head.next
        return self.__generate(node_list, 0, len(node_list) - 1)

    def __generate(self, node_list, start, end):
        if start > end:
            return None
        if start == end:
            return TreeNode(node_list[start])
        mid = (start + end) // 2
        root = TreeNode(node_list[mid])
        root.left = self.__generate(node_list, start, mid - 1)
        root.right = self.__generate(node_list, mid + 1, end)
        return root
