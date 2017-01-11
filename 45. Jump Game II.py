'''
class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ###set original step as [n]*n
        ###every iteration we propogate once and update step if any step[j] gets lower
        if not nums:return 0
        n=len(nums)
        if n==1:return 0
        step=[n]*n;
        step[0]=0
        for i in range(n-1):
            for j in range(i+1,min(i+nums[i]+1,n)):
                step[j]=min(step[j],step[i]+1)
                if j==n-1:
                    return step[n-1]
        return step[n-1]

'''
class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ###every time take one jump to the furtherest it can reach and update search range to the next segmentation
        ans = lastIdx = nextIdx = 0
        while nextIdx < len(nums) - 1:
            ans += 1
            lastIdx, nextIdx = nextIdx+1, max(i + nums[i] for i in xrange(lastIdx, nextIdx + 1))
        return ans