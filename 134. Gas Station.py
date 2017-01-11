class Solution(object):
'''
    def arun(self,start_pos,circlebalance,n):
        go=0;
        newround=circlebalance[start_pos:n]+circlebalance[0:start_pos]
        for i in range(n):
            go+=newround[i];
            if go<0:
                return False
        return True
            
    
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        if not gas: return -1
        n=len(gas)
        if sum(gas)<sum(cost):return -1
        index=range(n);
        balance=[0]*n;
        for i in index:
            balance[i]=gas[i]-cost[i]
        cnt=0;
        circlebalance=list(balance);
        while cnt<n:
            balancemax=max(balance);
            max_index=balance.index(balancemax);
            start_pos=index[max_index]
            if self.arun(start_pos,circlebalance,n):
                return start_pos
            else:
                balance.pop(max_index);
                index.pop(max_index);
            cnt+=1;
'''

 
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        ####two main assumptions:
        ####fail if sum(gas)< sum(cost), otherwise must succeed
        ####if start from station i and fail at station j, then any start point from between will fail
        if not gas: return -1
        if sum(gas)<sum(cost):return -1
        n=len(gas)
        start_pos=0;go=0;cur_pos=0;
        while cur_pos<n:
            go+=gas[cur_pos]-cost[cur_pos];
            cur_pos+=1
            if go<0:
                go=0;
                start_pos=cur_pos
            
        return start_pos
