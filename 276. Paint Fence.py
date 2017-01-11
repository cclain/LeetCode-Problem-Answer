class Solution(object):
    def numWays(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        ##spcial case for n=4,k=2:0101,1010;0010,1101,1001,0110,0100,1011,0011,1100,
        ##we can paint one fence or two fences in same color at each time with (k-1) choices
        if n==0 or k==0:return 0
        if n==1:return k
        if n==2:return k*k
        way2,way1=k*k,k
        cnt=3;
        while cnt<=n:
            way2,way1=(way2+way1)*(k-1),way2
            cnt+=1
        return way2