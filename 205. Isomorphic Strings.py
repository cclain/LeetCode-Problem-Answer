class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        sdict={}
        tdict={}
        for i in range(len(s)):
            if s[i] in sdict:
                if sdict[s[i]]==t[i]:
                    continue
                else:
                    return False
            else:
                if t[i] in tdict:
                    return False
                else:
                    sdict[s[i]]=t[i]
                    tdict[t[i]]=s[i]
                    
                             
        return True