# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        

        dummy = ListNode()
        merged_curr = dummy

        curr1 = list1
        curr2 = list2

        while curr1 and curr2:
            if curr1.val <= curr2.val:
                merged_curr.next = curr1
                curr1 = curr1.next

            else:
                merged_curr.next = curr2
                curr2 = curr2.next

            merged_curr = merged_curr.next

        if curr1 or curr2:
            merged_curr.next = curr1 or curr2

        return dummy.next
                

