class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:return 0
        n=len(prices)
        if n==1:return 0
        cur_max=0;
        all_profit=0;
        for i in range(1,n):
            temp=prices[i]-prices[i-1]
            if temp>0:
                cur_max+=temp;
            else:
                all_profit+=cur_max
                cur_max=0
        return all_profit+cur_max