# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """

        1,2,3,4,5  length = 5 n = 2 removal = 3
        ^ ^ ^ ^
        itll go one over so just keep a pointer of the one before it 

        basically loop to get count of the list 
        then do count - n to find out the node before the one you want to skip

        if the count == n then that means your removing the head so just return head.next

        """

        length = 0
        dummy = head

        while dummy:
            length +=1
            dummy = dummy.next

        if length == n:
            return head.next

        removal = length - n

        prev = None
        curr = head
        count = 0

        while count < removal:
            count +=1
            prev = curr 
            curr = curr.next 

        prev.next = curr.next

        return head



        