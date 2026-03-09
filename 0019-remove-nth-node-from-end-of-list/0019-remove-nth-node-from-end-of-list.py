# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        loop through linked list to get the count
        after that the target is count - n
        so then loop again until count == target
        that means you are on the node before what you should remove
        so change that next to be .next.next

        1 -> 2 -> 3 -> 4 -> 5       n = 2
                       ^
                  


        count = 3
        target = 3
        """
        count = 0

        curr = head

        while curr:
            count +=1 
            curr = curr.next

        if count == n:
            return head.next

        target = count - n

        count = 0
        node = head
        prev = None
        while count < target:
            count +=1
            prev = node
            node = node.next

        prev.next = node.next

        

        return head
            

