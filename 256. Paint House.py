class Solution(object):
    def minCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        ###color cost is the cost ending in color r,b,g
        if not costs:return 0
        n=len(costs)
        if n==1:return min(costs[0])
        colorcost=[costs[0][0],costs[0][1],costs[0][2]]
        for i in range (1,n):
            r=costs[i][0]+min(colorcost[1],colorcost[2])
            b=costs[i][1]+min(colorcost[0],colorcost[2])
            g=costs[i][2]+min(colorcost[0],colorcost[1])
            colorcost=[r,b,g]
        return min(r,b,g)