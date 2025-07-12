// RegularExpressionMatching.java
import java.util.HashMap;

class Solution {
    private HashMap<String, Boolean> memory; // memoization -> key: str(i) + str(), val: True/False

    public boolean isMatch(String s, String p) {
        this.memory = new HashMap<>();
        return checkMatch(0, 0, s, p);
    }

    // helper function to be called recursively
    private boolean checkMatch(int i, int j, String s, String p) {
        // concat pointers i and j into a string to serve as key
        String key = i + "" + j;

        // if match value is already store in memory, return value
        if (this.memory.containsKey(key)) {
            return this.memory.get(key);
        }

        // check if we reached end of both, string and pattern
        if (j == p.length()) {
            return i == s.length();
        }

        // check if there's match between chars. we must be within string s bounds handle '.' wildcard on pattern
        boolean charsMatch = (i < s.length() && (s.charAt(i) == p.charAt(j) || p.charAt(j) == '.'));

        boolean matchingResult;
        // check if there's an '*' after current pattern char
        if ((j + 1) < p.length() && p.charAt(j + 1) == '*') {
            // if there is, we either ignore it (matches 0 times) or use it 1 or more times
            // if we ignore it, we move to char after '*' in p, while staying on the same s char
            // if we use it, it means there's a match, so we move to the next char on string s,
            // we stay on the same p char
            matchingResult = (charsMatch && checkMatch(i + 1, j, s, p)) || checkMatch(i, j + 2, s, p);
        } else {
            // if there's no '*', we look for a 1 to 1 match. if there is, we move to next char on both s and p
            matchingResult = charsMatch && checkMatch(i + 1, j + 1, s, p);
        }

        this.memory.put(key, matchingResult); // store matching result in memo
        return matchingResult; // return matching result
    }
}
