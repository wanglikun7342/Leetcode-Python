from typing import List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def splitListToParts(self, root: ListNode, k: int) -> List[ListNode]:
        num = k
        result = []
        head = root
        size = 0
        while head is not None:
            size += 1
            head = head.next
        extra = size % k
        length = size // k
        cur_node = root
        start_node = cur_node
        while cur_node is not None:
            if extra > 0:
                for i in range(1, length + 1):
                    cur_node = cur_node.next
                extra -= 1
            else:
                for i in range(1, length):
                    cur_node = cur_node.next
            next_node = cur_node.next
            result.append(start_node)
            num-=1
            cur_node.next = None
            cur_node = next_node
            start_node = cur_node
        while num >= 1:
            num-=1
            result.append(None)
        return result
