class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        wordlist={};
        for x in strs:
            xsort=''.join(sorted(x))
            if xsort in wordlist:
                wordlist[xsort]+=[x];
            else:
                wordlist[xsort]=[x];
        return [wordlist[group] for group in wordlist]