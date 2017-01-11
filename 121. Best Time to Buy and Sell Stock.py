class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        ###profit can only go up not go down, hence when cur_max<0, reset it to zero
        ###this scenario also indicates that we have touched a lowest price of all previous prices
        if not prices:return 0
        n=len(prices);
        if n==1:return 0
        cur_max=all_max=0;
        for i in range(1,n):
            cur_max=max(0,cur_max+prices[i]-prices[i-1]);
            all_max=max(all_max,cur_max)
        return all_max