class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        cur_max=all_max=nums[0];
        for i in range(1,n):
            cur_max=max(cur_max+nums[i],nums[i]);
            all_max=max(cur_max,all_max)
        return all_max