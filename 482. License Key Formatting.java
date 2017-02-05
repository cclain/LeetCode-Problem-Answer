public class Solution {
    public String licenseKeyFormatting(String s, int k) {
        StringBuilder sb= new StringBuilder();
        int cnt=0;
        for (int i=s.length()-1;i>=0;i--){
            if (s.charAt(i)!='-'){
                sb.append(s.charAt(i));
                cnt++;
                if (cnt==k){
                    sb.append('-');
                    cnt=0;
                }
            }
        }
        sb=sb.reverse();
        if (sb.length()>0 && sb.charAt(0)=='-') sb.deleteCharAt(0);
        return sb.toString().toUpperCase();
        
    }
}