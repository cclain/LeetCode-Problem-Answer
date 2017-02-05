class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        n1=len(num1)
        n2=len(num2)
        if n1==0:return num2
        if n2==0:return num1
        if n1<n2:
            num1='0'*(n2-n1)+num1
        else:
            num2='0'*(n1-n2)+num2
            
        carry=0;
        result="";
        for i in range(max(n1,n2))[::-1]:
            temp=int(num1[i])+int(num2[i])+carry;
            if temp>=10:
                temp-=10;
                carry=1;
            else:
                carry=0;
            result+=str(temp);
        return (result+'1')[::-1] if carry==1 else result[::-1]
                
        
