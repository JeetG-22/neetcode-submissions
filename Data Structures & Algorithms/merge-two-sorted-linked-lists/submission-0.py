# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        combined = []
        while list1:
            combined.append(list1.val)
            list1 = list1.next
        while list2:
            combined.append(list2.val)
            list2 = list2.next
        combined.sort()

        sorted_ll = ListNode(-1)
        temp = sorted_ll
        for val in combined:
            temp.next = ListNode(val)
            temp = temp.next
        return sorted_ll.next
            
        