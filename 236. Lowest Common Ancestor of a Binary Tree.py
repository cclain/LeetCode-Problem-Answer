# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        stack=[root];
        parent_dict={root:None};
        while p not in parent_dict or q not in parent_dict:
            node=stack.pop();
            if node.left:
                parent_dict[node.left]=node;
                stack.append(node.left);
            if node.right:
                parent_dict[node.right]=node;
                stack.append(node.right); 
        ancestor=set();
        while p:
            ancestor.add(p);
            p=parent_dict[p];
        while q:
            if q in ancestor:
                break
            else:
                q=parent_dict[q]
        return q