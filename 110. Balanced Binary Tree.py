# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root: return True
        leftdepth=self.treedepth(root.left);
        rightdepth=self.treedepth(root.right);
        return (leftdepth-rightdepth<2 and rightdepth-leftdepth<2) and self.isBalanced(root.left) and self.isBalanced(root.right)
          
        
        
    def treedepth(self, root):
        if not root: return 0
        else: return max(self.treedepth(root.left),self.treedepth(root.right))+1




#############################################################

class UnbalancedTree(BaseException):
    pass
class Solution(object):
    def get_height(self, root):
        if not root:
            return 0
        left = self.get_height(root.left)
        right = self.get_height(root.right)
        if abs(left - right) > 1:
            raise UnbalancedTree() 
        return max(left, right) + 1
        
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        try:
            self.get_height(root)
        except UnbalancedTree:
            return False
        return True