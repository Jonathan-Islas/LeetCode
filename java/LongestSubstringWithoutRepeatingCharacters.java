// LongestSubstringWithoutRepeatingCharacters.java
class Solution {
    public int lengthOfLongestSubstring(String s) {
        if(s.length() == 0)
            return 0;
        int left = 0;
        int right = 0; 
        int max_len = 0;
        Set<String> unique_chars = new HashSet<>();
        do{
            if(!unique_chars.contains(String.valueOf(s.charAt(right)))){
                unique_chars.add(String.valueOf(s.charAt(right)));
                max_len = Math.max(max_len,unique_chars.size());
                right+=1;
            }else{
                unique_chars.remove(String.valueOf(s.charAt(left)));
                left+=1;
            }
        }while(right < s.length());
        return max_len;
    }
}
