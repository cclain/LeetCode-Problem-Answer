class Solution(object):
    def isOneEditDistance(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        n,m=len(s),len(t);
        if abs(n-m)>1:return False
        if s==t:return False
        cnt=0;
        if n==m:
            for i in range(n):
                if s[i]==t[i]:pass
                else:cnt+=1
                if cnt>1: return False
            if cnt==1:return True
        else:
            if n<m:
                s,t=t,s
                n,m=m,n
            j=0;
            for i in range(n):
                if i==n-1:
                    if cnt==0:return True
                    else: return s[i]==t[j]
                if s[i]==t[j]:pass;
                else:
                    cnt+=1
                    j-=1;
                if cnt>1:return False
                j+=1;