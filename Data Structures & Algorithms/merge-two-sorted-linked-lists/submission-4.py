# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head1, head2 = list1, list2
        new_head = temp = ListNode()
        while head1 or head2:
            if not head1:
                temp.next = head2
                head2 = head2.next
            elif not head2:
                temp.next = head1
                head1 = head1.next
            elif head1.val < head2.val:
                temp.next = head1
                head1 = head1.next
            else:
                temp.next = head2
                head2 = head2.next
            temp = temp.next
        return new_head.next
            
            

        
        