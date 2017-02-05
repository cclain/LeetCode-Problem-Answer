##DP with record
class Solution(object):
    def canWin(self, s):
        """
        :type s: str
        :rtype: bool
        """
        n=len(s)
        record={}
        def tryall(s):
            if s not in record:
                record[s]=any(s[i]==s[i+1]=='+' and not tryall(s[:i]+'--'+s[i+2:]) for i in range(n-1))
            return record[s]
        return tryall(s)
            
'''
##DP without record
class Solution(object):
    def canWin(self, s):
        return any(s[i:i+2] == '++' and not self.canWin(s[:i] + '-' + s[i+2:]) for i in range(len(s)))
'''

