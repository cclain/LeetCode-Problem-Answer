class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        zlist=[]
        for i in range(n):
            if nums[i]==0: zlist.append(i)
        nz=len(zlist)
        for i in range(nz):
            nums.pop(zlist[i]-i)
        nums+=[0]*nz

'''
####move all none-zero element to the front and add remain zeros in the end
class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        int j=0;
        for(int i=0;i<nums.size();i++){
            if (nums[i]!=0){
                nums[j++]=nums[i];
            }
        }
        for(;j<nums.size();j++){
            nums[j]=0;
        }
    }
};
'''