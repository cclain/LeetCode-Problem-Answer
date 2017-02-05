class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels=set({'a','e','i','o','u','A','E','I','O','U'})
        slist=list(s)
        n=len(s)
        if n<2:return s
        p1=0;p2=n-1
        while p1<p2:
            if slist[p1] in vowels:
                while slist[p2] not in vowels:
                    p2-=1
                    if not p1<p2:break
                slist[p1],slist[p2]=slist[p2],slist[p1]
                p1+=1;
                p2-=1
            else:
                p1+=1
        return ''.join(slist)