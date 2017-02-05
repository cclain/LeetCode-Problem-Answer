// The only way in this case to determine if an anagram appears is when count==0 and substring length=p.length()
public class Solution {
    public List<Integer> findAnagrams(String s, String p) {
        List<Integer> list=new ArrayList<>();
        if (s==null || s.length()==0) return list;
        
        int[] hash=new int[128];
        for (char ch :p.toCharArray()){
            hash[ch]++;
        }
        int left=0,right=0,count=p.length();
        
        while(right<s.length()){
            if (hash[s.charAt(right)]>0){
                count--;
            }
            hash[s.charAt(right)]--;
            right++;
            if (count==0) list.add(left);
            
            if (right-left==p.length()){
                if (hash[s.charAt(left)]>=0) count++;
                hash[s.charAt(left)]++;
                left++;
            }
        }
        return list;
    }
}