class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        best=0
        res=""
        for i in xrange(0,len(s)):
            temp=self.helper(s,i,i)
            if len(temp)>best:
                best=len(temp)
                res=temp
            temp=self.helper(s,i,i+1)
            if len(temp)>best:
                best=len(temp)
                res=temp
        return res
        
    def helper(self,s,l,r):
        while l>=0 and r<len(s) and s[l]==s[r]:
            l-=1;
            r+=1;
        return s[l+1:r]

'''
public class Solution {
    
    public String longestPalindrome(String s) {
        int maxlen=0;
        String result="";
        String temp="";
        for(int i=0;i<s.length();i++){
            temp=helper(s,i,i);
            if (temp.length()>maxlen) {
                maxlen=temp.length();
                result=temp;
            }
            temp=helper(s,i,i+1);
            if (temp.length()>maxlen){
                maxlen=temp.length();
                result=temp;
            }
        }
        return result;
        
    }
    
    private String helper(String s,int l,int r){
        while(l>=0 && r<s.length() && s.charAt(l)==s.charAt(r)){
            l--;
            r++;
        }
        return s.substring(l+1,r);
    }
}
'''
            
            