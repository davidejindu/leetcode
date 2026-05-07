# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        create a dummy node to keep track of head of the new list
        then with the curr that will be used to create a new list
        
        loop while you have both nodes 
        compare the two nodes if node1 is smaller than node 2
        add curr.next to node1 and increment node1
        else add node2 to curr.next increment node2

        now if not node1 then set the whole rest of curr.next to that node


        """
        dummy = ListNode()
        curr = dummy
        node1, node2 = list1, list2

        
        while node1 and node2:
            if node1.val > node2.val:
                curr.next = node2
                node2 = node2.next
            else:
                curr.next = node1
                node1 = node1.next

            curr = curr.next

        if not node1:
            curr.next = node2
        else:
            curr.next = node1

        return dummy.next

