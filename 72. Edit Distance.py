class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        n1,n2=len(word1),len(word2);
        if n1==0 or n2==0:return abs(n1-n2)
        ##initialization        
        dptable=[[0 for i in range(n1+1)] for j in range(n2+1)]
        dptable[0]=range(n1+1)
        for i in range(n2+1):
            dptable[i][0]=i
        for j in range(1,n1+1):
            for i in range(1,n2+1):
                if word1[j-1]==word2[i-1]:
                    dptable[i][j]=dptable[i-1][j-1];
                else:
                    dptable[i][j]=min(dptable[i-1][j-1]+1,dptable[i-1][j]+1,dptable[i][j-1]+1)
        return dptable[n2][n1]

'''
dptable=[[0]*(n1+1)]*(n2+1)
dptable=[[0 for i in range(n1+1)] for j in range(n2+1)]
#the first way to create list results in bugs. Because such list item should be immutable, or to say dptable[i] and dptable[i+1] share the same reference.
