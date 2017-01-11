class Solution(object):
    def minCostII(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        ####we only need to keep record of cost for two smallest cost of last trial
        ####for current house, if not same color, cost=costs[cnt-1[[i]+min1
        ####if same color,cost=costs[cnt-1[[i]+min2
        if not costs:return 0
        n=len(costs);
        if n==1:return min(costs[0])
        k=len(costs[0]);
        templist=list(costs[0]);
        cnt=2
        while cnt<=n:
            min1=min(templist)
            min_pos1=templist.index(min1);
            templist.pop(min_pos1)
            min2=min(templist)
            templist=[0]*k
            for i in range(k):
                if i!=min_pos1:
                    templist[i]=costs[cnt-1][i]+min1
                else:
                    templist[i]=costs[cnt-1][i]+min2
            cnt+=1
        return min(templist)