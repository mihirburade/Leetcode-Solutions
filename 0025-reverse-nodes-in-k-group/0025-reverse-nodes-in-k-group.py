# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """

        dummy=ListNode(0)
        dummy.next=head
        group_previous=dummy
        
        while True:
                kth=group_previous
                for _ in range(k):
                    kth=kth.next

                    if kth is None:
                        return dummy.next

                group_next=kth.next
                previous=group_next
                current=group_previous.next

                while current!=group_next:
                    next_node=current.next
                    current.next=previous
                    previous=current
                    current=next_node

                old_first=group_previous.next
                group_previous.next=kth
                group_previous=old_first
        return head