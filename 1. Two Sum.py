class Solution(object):
    def twoSum(self, nums, target):
        sort_nums=sorted(nums);
        index_dict={};
        for i in range(len(sort_nums)):
            index_dict[str(sort_nums[i])]=i;
        for j in range(len(sort_nums)):
            find_num=target-sort_nums[j];
            if index_dict.has_key(str(find_num)) and find_num!=sort_nums[j] :
                return nums.index(sort_nums[j]),nums.index(find_num)
                break
            elif index_dict.has_key(str(find_num)) and (find_num==sort_nums[j] and sort_nums[j]==sort_nums[j+1]):
                a1=nums.index(find_num);
                nums.remove(find_num);
                a2=nums.index(find_num)
                return a1,a2+1
                break