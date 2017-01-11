# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:return True
        stack1=[root];
        orderlist1=[root];
        stack2=[root];
        orderlist2=[root];
        cnt1=0;
        cnt2=0;
        while len(stack1)!=0:
            node1=stack1.pop();
            node2=stack2.pop();
            if node1.left:
                stack1.append(node1.left);
                orderlist1.append(node1.left.val);
                cnt1+=1;
            if node2.right:
                stack2.append(node2.right);
                orderlist2.append(node2.right.val);
                cnt2+=1
            if cnt1!=cnt2 or orderlist1[cnt1] != orderlist2[cnt2]:
                return False
            if node1.right:
                stack1.append(node1.right);
                orderlist1.append(node1.right.val);
                cnt1+=1;
            if node2.left:
                stack2.append(node2.left);
                orderlist2.append(node2.left.val);
                cnt2+=1;
            if cnt1!=cnt2 or orderlist1[cnt1] != orderlist2[cnt2]:
                return False
        return True