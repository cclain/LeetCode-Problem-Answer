# Definition for a  binary tree node
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
###build a search function, every time search the right subtree for all its left children
class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.stack=[]
        self.search(root)

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.stack

    def next(self):
        """
        :rtype: int
        """
        if not self.stack:return None  
        node=self.stack.pop()
        self.search(node.right)
        return node.val
        
        
    def search(self,root):
        if not root:return
        while root:
            self.stack.append(root)
            root=root.left

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())