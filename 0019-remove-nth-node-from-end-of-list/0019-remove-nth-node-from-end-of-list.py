# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        count=0
        current=head
        node=0

        while current:
            count+=1
            current=current.next

        if n==count:
            return head.next
        current = head
            
        while count-n-1>node:
            current=current.next
            node+=1

        current.next=current.next.next
        return head

        