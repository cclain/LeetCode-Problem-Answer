# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        ###first remove val if they exist in the start of the list
        ###then propogate
        if head==None:return head
        while head.val==val:
            head=head.next
            if head==None:return head
        p1=head;p2=p1.next
        while p2!=None:
            if p2.val==val:
                p2=p2.next
                p1.next=p2
            else:
                p1=p2;
                p2=p1.next
        return head