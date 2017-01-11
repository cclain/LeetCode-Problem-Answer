class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums:return False
        n=len(nums)
        if n==1:return True
        stack=[0];
        max_reach=0
        while max_reach<n-1:
            pos=stack.pop()
            if pos+nums[pos]>=n-1:
                return True
            elif nums[pos]==0:
                pass;
            else:
                if pos+nums[pos]<=max_reach:
                    pass
                else:
                    for i in range(max_reach+1,pos+nums[pos]+1):
                        stack.append(i)
                    max_reach=pos+nums[pos]
            if not stack: return False
        return True