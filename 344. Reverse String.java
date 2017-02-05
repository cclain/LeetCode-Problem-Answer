import java.util.*;
public class Solution {
    public String reverseString(String s) {
        char[] a=s.toCharArray();
        int i=0,j=s.length()-1;
        while(i<j){
            char temp=a[i];
            a[i]=a[j];
            a[j]=temp;
            i++;
            j--;
        }
        return new String(a);

    }
}