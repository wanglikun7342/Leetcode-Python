# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        cur = head
        node_list = []
        while cur is not None:
            node_list.append(cur)
            cur = cur.next

        for index in range(0, len(node_list)):
            j = index
            target = node_list[index].val
            while j >= 0 and target < node_list[j - 1].val:
                node_list[j].val = node_list[j - 1].val
                j -= 1
            node_list[j].val = target
        node_list.clear()
        return head
