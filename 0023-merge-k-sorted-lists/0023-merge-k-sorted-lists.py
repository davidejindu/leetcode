# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
"""
you want to go through two of the lists at a time and merge them in sorted order

after that you want to make lists[i] = to the new merged list and then return lists[len(lists) - 1] this should contain the last index that has all the merged values


[1,4,5],[1,3,4],[2,6]
          i        i + 1

merge(1,4,5) and merge(1,3,4)

make i + 1 = 1,1,3,4,4,5  now lists is 

[1,4,5], [1,1,3,4,4,5], [2,6]

merge(1,1,3,4,4,5) and merge(2,6)

[1,4,5],[1,1,3,4,4,5],  1,1,2,3,4,4,5,6


"""
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return

        for i in range(len(lists) - 1): 
            l1, l2 = lists[i], lists[i + 1]
            lists[i + 1] = self.mergeList(l1,l2)

        return lists[-1]


    def mergeList(self,l1, l2):
        dummy = ListNode()
        curr = dummy

        while l1 and l2:
            if l1.val < l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next

        if l1:
            curr.next = l1
        if l2:
            curr.next = l2

        return dummy.next
        