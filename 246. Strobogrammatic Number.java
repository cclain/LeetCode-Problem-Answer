public class Solution {
    public boolean isStrobogrammatic(String num) {
        if(num.length()==0 || num==null) return false;
        HashMap<Character,Character> map=new HashMap<Character,Character>();
        map.put('0','0');
        map.put('1','1');
        map.put('8','8');
        map.put('6','9');
        map.put('9','6');
        int n=num.length();
        for (int i=0; i<=n/2;i++){
            if(!map.containsKey(num.charAt(i)) || map.get(num.charAt(i))!=num.charAt(n-i-1))  return false;
        }
        return true;
    }
}



//Another smart solution
public class Solution {
    public boolean isStrobogrammatic(String num) {
        for (int i=0, j=num.length()-1; i <= j; i++, j--)
            if (!"00 11 88 696".contains(num.charAt(i) + "" + num.charAt(j)))
                return false;
        return true;
    }
}