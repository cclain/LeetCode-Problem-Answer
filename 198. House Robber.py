class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        house=len(nums)
        if house==1:return nums[0]
        if house==2:return max(nums[0],nums[1])
        b,a=max(nums[0],nums[1]),nums[0]
        for i in range(2,house):
            if b==a:
                b,a=a+nums[i],b
            else:
                b,a=max(b,a+nums[i]),b 
        return b