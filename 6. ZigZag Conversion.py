
class Solution(object):
    def convert(self, s, numRows):
        if numRows>1 and len(s)>0:
            display=['' for x in range(numRows)];
            cut=2*(numRows-1);
            while (len(s)>=cut):
                ss=s[:cut];
                for i in range(cut):
                    if i<=numRows-1:
                        display[i]=display[i]+ss[i];
                    else:
                        temprow=numRows-(i+1)%numRows;
                        display[temprow-1]=display[temprow-1]+ss[i];
                s=s[cut:];
            if len(s)>0:
                for i in range(len(s)):
                    if i<=numRows-1:
                        display[i]=display[i]+s[i];
                    else:
                        temprow=numRows-(i+1)%numRows;
                        display[temprow-1]=display[temprow-1]+s[i];
            result='';
            for i in range(numRows):
                result+=display[i];  
            return result
        else:
            return s     

            
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """