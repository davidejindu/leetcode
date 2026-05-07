# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """
    have two nodes
    one slow 
    one fast
    if they are equal then we know there is a cycle since fast one shouldnt be same as slow unless there is a cycle

        """

        fast = slow = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

            if slow == fast:
                return True

        return False