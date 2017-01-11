class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n==1:return True
        past={n};
        sqsum=0;
        while n!=1:
            while n!=0:
                a=n%10;
                sqsum+=a*a
                n=n/10;
            if sqsum in past:
                return False
            else:
                past.add(sqsum)
            n=sqsum;
            sqsum=0;
        return True