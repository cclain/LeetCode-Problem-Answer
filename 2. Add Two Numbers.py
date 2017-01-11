
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        sumlist=ListNode(0)
        cur1=l1;
        cur2=l2;
        cur3=sumlist;
        carr=0;
        while( cur1!=None or cur2!= None):
            if cur1==None:
                x=0
            else:
                x=cur1.val
                cur1=cur1.next
            if cur2==None:
                y=0
            else:
                y=cur2.val
                cur2=cur2.next
            allsum=x+y+carr;
            cur3.val=allsum%10;
            carr=allsum/10;
            if cur1!=None or cur2!= None or carr>0:
                cur3.next=ListNode(0)
                cur3=cur3.next
        if carr>0:
            cur3.val=carr
        
        return sumlist
        
        
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """