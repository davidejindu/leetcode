# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
"""
remove the nth last node from the linkedlist

1 2 3 4 5 
      ^

count = 3
removal_point = 3

basically loop through linkedlist to get the count
after that go till you get to length of list - n
when you get to len of list - n set the next node to the one after nth node

if the length of list == n return head.next


"""
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        count = 0
        curr = head

        while curr:
            count +=1
            curr = curr.next

        #if n == len of list we just return everything except the head
        if n == count:
            return head.next

        #get removal point 
        removal_point = (count - n) - 1

        count = 0
        curr = head

        while count != removal_point:
            count +=1
            curr = curr.next

        curr.next = curr.next.next

        return head
        