# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:return []
        cnt=0
        trace=head
        while trace is not None:
            cnt+=1
            trace=trace.next
        return self.DivideandSort(head,cnt)
        
            
        
    def DivideandSort(self,head,length):
        if not head or not head.next:return head
        else:
            newlen=length/2
            l1pointer=l1head=ListNode(None)
            for i in range(newlen):
                l1pointer.next=head
                l1pointer=l1pointer.next
                head=head.next
            l1pointer.next=None
            l2head=head
            l1head=self.DivideandSort(l1head.next,newlen)
            l2head=self.DivideandSort(l2head,length-newlen)
            
        return self.Merge(l1head,l2head)
    
    def Merge(self,l1head,l2head):
        if l1head is None:return l2head
        if l2head is None:return l1head
        dummy=tail=ListNode(None)
        while l1head and l2head:
            if l1head.val<l2head.val:
                tail.next=l1head;
                tail=tail.next
                l1head=l1head.next
            else:
                tail.next=l2head;
                tail=tail.next
                l2head=l2head.next    
        if l1head:
            tail.next=l1head
        else:
            tail.next=l2head
        return dummy.next  
                
                
                    

                    
        
        
    
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None: return head
        if head.next is None:return head
        l1=head;l2=head;cur=head
        while l2 is not None and l2.next is not None:
            cur=l1
            l1=l1.next
            l2=l2.next.next
        cur.next=None
        l1head=self.sortList(head)
        l2head=self.sortList(l1)
        return self.Merge(l1head,l2head)
    ###Merge function results in too many recursion, hence can be changed with no recursion form
    def Merge(self,l1head,l2head):
        if l1head is None:return l2head
        if l2head is None:return l1head
        if l1head.val<l2head.val:
            l1head.next=self.Merge(l1head.next,l2head)
            return l1head
        else:
            l2head.next=self.Merge(l1head,l2head.next)
            return l2head
              


                    

                    
        
        
    
        