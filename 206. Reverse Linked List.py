# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

###iterative solution
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        prev=None
        while head:
            cur=head
            head=head.next
            cur.next=prev
            prev=cur
        return prev

###recursive solution
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        return self.reverse(head,prev=None)
        
    def reverse(self,head,prev):
        if not head:
            return prev
        
        next=head.next
        head.next=prev
        return self.reverse(next,head)