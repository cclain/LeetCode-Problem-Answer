class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ###anything XOR X twice is still itself
        result=0
        for x in nums:
            result^=x;
        return result