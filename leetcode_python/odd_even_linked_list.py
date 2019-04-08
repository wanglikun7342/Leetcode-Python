class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        odd_root = head
        if head is None:
            return odd_root
        even_root = head.next
        odd_cur = odd_root
        even_cur = even_root
        while odd_cur.next is not None and even_cur.next is not None:
            odd_cur.next = even_cur.next
            if odd_cur.next is not None:
                odd_cur = odd_cur.next
            even_cur.next = odd_cur.next
            even_cur = even_cur.next
        odd_cur.next = even_root
        return odd_root
