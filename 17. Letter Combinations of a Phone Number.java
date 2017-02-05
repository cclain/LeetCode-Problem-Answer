//This method use a temparay list to record updated string in every round, hence more space is required
public class Solution {
    private static String[] keys = { "", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz" };
    public List<String> letterCombinations(String digits) {
        List<String> result= new ArrayList<String>();
        if(digits.length()==0 || digits==null) return result;
        
        for (int i=0; i<digits.length();i++){
            String string_add=keys[digits.charAt(i)-'0'];
            List<String> templist=new ArrayList<String>();
            for (int j=0;j<string_add.length();j++){
                for (int n=0;n<result.size();n++){
                    templist.add(result.get(n)+string_add.charAt(j));
                }
            }
            result=templist;
        }
        return result;
    }
}


//Use a linkedlist to implement FIFO queue, no extra space needed, much faster
public class Solution {
    private static String[] keys = { "", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz" };
    public List<String> letterCombinations(String digits) {
        LinkedList<String> result= new LinkedList<String>();
        if(digits.length()==0 || digits==null) return result;
        
        
        result.add("");
        for (int i=0;i<digits.length();i++){
            String str_add=keys[digits.charAt(i)-'0'];
            while(result.peek().length()==i){
                String toBeAdd=result.remove();
                for(int j=0;j<str_add.length();j++){
                    result.add(toBeAdd+str_add.charAt(j));
                }
                
            }
        }
        return result;
    }
}