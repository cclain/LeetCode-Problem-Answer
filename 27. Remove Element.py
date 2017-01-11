class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        cnt=0;
        n=len(nums)
        for x in nums:
            if x!=val:
                nums[cnt]=x;
                cnt+=1;
        ##pop out the extra val (n-cnt) times
        for i in range(n-cnt):
            nums.pop(cnt)