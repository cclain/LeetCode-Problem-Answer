class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # //we need to implement a tree-time counter(base 3) that if a bit appears three time ,it will be zero.
        #curent  income  ouput
        # ab      c/c       ab/ab
        # 00      1/0       01/00
        # 01      1/0       10/01
        # 10      1/0       00/10
        #a=~abc+a~b~c;
        #b=~a~bc+~ab~c;
        a=0;
        b=0;
        for c in nums:
            a,b=(~a&b&c)|(a&~b&~c),(~a&~b&c)|(~a&b&~c);
        #we need find the number that is 01,10 => 1, 00 => 0.
        return a|b;
'''
public class Solution {
    public int singleNumber(int[] A) {
        int ones = 0, twos = 0;
        for(int i = 0; i < A.length; i++){
            ones = (ones ^ A[i]) & ~twos;
            twos = (twos ^ A[i]) & ~ones;
        }
        return ones;
    }
}
'''