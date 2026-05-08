# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        basically merge sort
        keep sorting two of the lists
        then change lists = to the merged lists keep looping until 1 list
        meaning you have merged all of it then return


        [1,4,5],[1,3,4],[2,6]
                          i

        temp_ lists = [[1,1,3,4,4,5], [2,6]]
        
        lists = [[1,1,3,4,4,5], [2,6]]
                    i           i + 1
        temp_lists = [1,1,2,3,4,4,5,6]

        lists = temp_lists

      



        """
        if not lists:
            return None

        while len(lists) > 1:
            temp_lists = []

            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if (i + 1) < len(lists) else None
                temp_lists.append(self.mergedList(l1,l2))

            lists = temp_lists

        return lists[0]



    def mergedList(self,l1,l2):
        head = ListNode()
        dummy = head

        while l1 and l2:
            if l1.val < l2.val:
                dummy.next = l1
                l1 = l1.next
            else:
                dummy.next = l2
                l2 = l2.next

            dummy = dummy.next

        if not l1:
            dummy.next = l2
        else:
            dummy.next = l1

        return head.next