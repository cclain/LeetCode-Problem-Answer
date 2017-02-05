# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

####this is O(nlogn) solution
class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if not head:return None
        if not head.next:return TreeNode(head.val)
        slow=head;fast=head.next.next;
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        mid=slow.next
        slow.next=None
        root=TreeNode(mid.val)
        root.left=self.sortedListToBST(head)
        root.right=self.sortedListToBST(mid.next)
        return root
        
        