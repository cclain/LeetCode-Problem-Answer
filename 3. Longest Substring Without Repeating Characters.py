class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        n=len(s)

        if n==0:
            return 0
        else:
            templen=0;
            char_dict={}; 
            finlen=0;
            j=0;
            start=0
            for i in range(n):
                if char_dict.has_key(s[i])==False:
                        char_dict[s[i]]=i;
                        templen+=1;
                else:
                    newstart=char_dict[s[i]]+1;
                    for j in range(start,char_dict[s[i]]+1):
                        del char_dict[s[j]];
                    if finlen<templen:
                        finlen=templen;
                    char_dict[s[i]]=i;
                    start=newstart;
                    templen=len(char_dict);
            if finlen<templen:
                finlen=templen;
                    
            return finlen