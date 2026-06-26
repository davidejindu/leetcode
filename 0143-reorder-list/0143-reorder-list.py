# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
"""

input: 1 2 3 4
               
output 1 4 2 3 


input: 1 2 | 5 4 3
         ^
             ^

1 -> 5 -> 2 -> 4 -> 3

output 1 5 2 4 3

so first get the middle half of the list

after you get the middle half you want to reverse the second half of the list
"""
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        fast = slow = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        second = slow.next 
        slow.next = None
        prev = None

        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp 

        second = prev
        first = head



        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first = tmp1
            second = tmp2

        return head
        