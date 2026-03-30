# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        def reverse(head, k):
            prev = None
            curr = head
            while k:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
                k -= 1
            return prev

        count = 0
        node = head

        while node and count < k:
            node = node.next
            count += 1

        if count == k:
            new_head = reverse(head, k)
            head.next = self.reverseKGroup(node, k)
            return new_head

        return head
            