public class Solution {
    public List<String> findMissingRanges(int[] nums, int lower, int upper) {
        List<String> result=new ArrayList <String>();
        Long Lower=(long)lower;
        Long Upper=(long)upper;
        if (Lower>Upper) return result;
        for (int i=0;i<nums.length;i++){
            if (nums[i]<Lower) continue;
            if (nums[i]==Lower){
                Lower++;
                continue;
            }
            if (nums[i]<=Upper) {
                result.add(getRange(Lower,nums[i]-1));
                Lower=(long)nums[i]+1;
            
            }
            
        }
        if(Lower<=Upper) result.add(getRange(Lower,Upper));
        
        return result;
    }
    public String getRange(long Lower, long Upper){
        return (Lower==Upper)? String.valueOf(Upper) : String.valueOf(Lower) + "->" + String.valueOf(Upper);
    }
}