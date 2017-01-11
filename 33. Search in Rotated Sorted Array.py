class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:return -1
        head,end=0,len(nums)-1;
        while head<end:
            mid=head+(end-head)/2;
            if nums[mid]==target:return mid
            if nums[mid]>nums[end]:
                if nums[head]<=target<nums[mid]:
                    end=mid-1;
                else:
                    head=mid+1;
            elif nums[mid]<nums[end]:
                if nums[mid]<target<=nums[end]:
                    head=mid+1;
                else:
                    end=mid-1;
            else:
                end-=1;
        if nums[head]==target:return head
        else: return -1