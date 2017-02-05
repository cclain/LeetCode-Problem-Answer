class Solution(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:return True
        showdict={}
        for i in s:
            if i in showdict:
                showdict[i]+=1
            else:
                showdict[i]=1
        cnt=0;
        for key in showdict:
            if showdict[key]%2==1:
                cnt+=1
            if cnt>1:return False
        return True
'''
class Solution(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:return True
        showdict=set()
        for i in s:
            if i in showdict:
                showdict.discard(i)
            else:
                showdict.add(i)
        return len(showdict)==1 or len(showdict)==0
'''