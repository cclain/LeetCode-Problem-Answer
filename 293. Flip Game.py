##solution 1 search for all possible index while solution 2 use while loop to skip some positions
class Solution(object):
    def generatePossibleNextMoves(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        return [s[:i]+'--'+s[i+2:] for i in range(len(s)-1) if s[i]==s[i+1]=='+']
'''
class Solution(object):
    def generatePossibleNextMoves(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        n=len(s)
        if n==0 or n==1:return []
        result=[];
        pos=0;
        while pos<n-1:
            if s[pos]=='+':
                if s[pos+1]=='+':
                    result.append(s[:pos]+'--'+s[pos+2:]);
                    pos+=1
                else:
                    pos+=2
            else:
                pos+=1
        return result
'''