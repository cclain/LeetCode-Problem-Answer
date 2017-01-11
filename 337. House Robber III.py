# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.d={};
        
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        ###choose from root+root.sub-subtree or root.subtree
        ###however time limit exceeds
        ''''
        if not root:return 0
        val=0
        if root.left:
            val+=self.rob(root.left.left)
            val+=self.rob(root.left.right)
        if root.right:
            val+=self.rob(root.right.left)
            val+=self.rob(root.right.right)
        return max(root.val+val,self.rob(root.left)+self.rob(root.right))
        '''
        return self.robby(root)
        
    def robby(self,root):
        d=self.d
        if not root:return 0
        if root in d: return d[root]
        val=0
        if root.left:
            a=self.robby(root.left.left)
            d[root.left.left]=a;
            val+=a;
            a=self.robby(root.left.right)
            d[root.left.right]=a;
            val+=a;
        if root.right:
            a=self.robby(root.right.left)
            d[root.right.left]=a;
            val+=a;
            a=self.robby(root.right.right)
            d[root.right.right]=a;
            val+=a
        a1,a2=self.robby(root.left),self.robby(root.right)
        d[root.left]=a1;
        d[root.right]=a2;
        d[root]=max(root.val+val,a1+a2)
        return d[root]