class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        pleft={"(":")","[":"]","{":"}"}
        pright={")","]","}"}
        stack=[]
        for ch in s:
            if ch in pleft:
                stack.append(ch)
                
            elif ch in pright:
               if not stack:return False
               if pleft[stack.pop()]!=ch:return False
        return True if not stack else False


####java solution

public class Solution{
    public boolean isValid(String s){
        Stack<Character> stack=new Stack<Character>();
        for (int i=0;i<s.length();i++){
            if (s.charAt(i)=='(')
                stack.push(')');
            else if (s.charAt(i)=='[')
                stack.push(']');
            else if (s.charAt(i)=='{')
                stack.push('}');
            else if (stack.empty() || stack.pop()!=s.charAt(i))
                return false;
        }
        return stack.empty();
    }
}