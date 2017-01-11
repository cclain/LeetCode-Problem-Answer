class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        lo, hi = 0, len(nums)-1
        while lo < hi:
            mid = lo + (hi - lo)/2
            if nums[mid] == target:
                return True
            if nums[mid] > nums[hi]:
                if nums[lo] <= target < nums[mid]:
                    hi = mid-1
                else:
                    lo = mid + 1
            elif nums[mid] < nums[hi]:
                if nums[mid] < target <= nums[hi]:
                    lo = mid + 1
                else:
                    hi = mid-1
            else:
                hi -= 1
        return lo < len(nums) and nums[lo] == target