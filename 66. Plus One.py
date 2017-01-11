class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        n=len(digits)
        pos=n-1;
        while pos>=0 :
            if digits[pos]==9:
                digits[pos]=0;
                pos-=1;
            else:
                digits[pos]+=1;
                break
        
        if pos==-1:return [1]+digits;
        else:return digits