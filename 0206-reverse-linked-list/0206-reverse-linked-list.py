# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        """
        <- 1  2 -> 3 -> 4 -> 5
           pv   
              tp  
               c
        
             

        dont i need a prev which starts as None and curr which is head
        after that i need to make curr = curr.next the make 

        """

        prev = None
        curr = head

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        return prev
            
            
