class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ###the majority will remain positive in counting, otherwise revise majority
        majority=nums[0]
        cnt=1
        n=len(nums)
        for i in range(1,n):
            if nums[i]!=majority:
                cnt-=1
                if cnt<0:
                    cnt=0;
                    majority=nums[i]
            else:
                cnt+=1
        return majority