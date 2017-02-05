public class Solution {
    public int[] productExceptSelf(int[] nums) {
        if(nums.length==0 || nums==null) return nums;
        int n=nums.length;
        int[] out=new int[n];
        int temp=1;
        out[0]=1;
        for (int i=1;i<n;i++){
            out[i]=out[i-1]*nums[i-1];
        }
        temp=1;
        for (int i=n-1;i>0;i--){
            temp*=nums[i];
            out[i-1]*=temp;
        }
        return out;
    }
}