class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:return ""
        strlen=[len(string) for string in strs]
        strmin=min(strlen)
        n=len(strlen)
        if strmin==0:return ""
        cnt=0
        prefix=""
        while cnt<=strmin-1:
            ch=strs[0][cnt]
            for i in range(1,n):
                if ch!=strs[i][cnt]:return prefix
            cnt+=1
            prefix+=ch
        return prefix