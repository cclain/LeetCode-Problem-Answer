class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        indicator=1
        digit=[];
        
        if x<0:
            x=-1*x
            indicator=-1
        if x==0:
            return 0
        else:
            while(x!=0):
                digit.append(x%10); 
                x=x/10;
            result=0
            n=len(digit)
            for i in range(n):
                result+=digit[i]*pow(10,n-i-1)
            if n<10: 
                return result*indicator
            elif result>pow(2,31):
                return 0
            else:
                return result*indicator      