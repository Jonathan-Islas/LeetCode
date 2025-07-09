# ANALYSIS HERE
        # We receive a string s

        # Requrements:
        # To find the longest substring that has no repeating chars
        # return the length of the longest substring

        # ToDo 
        # Iterrate the string
        # obtain or save a substring with unique chars
        # Check if substring is valid
        # compare the new substring length with the current max length
        # if the new length is greater than current max, update max length
        # return max length 

        # Constraints
        # s is an alphanumeric string that can contain symbols and spaces
        
        #  |     |
        # a b c a b c b b

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0 # window's left pointer
        right = 0 # window's right pointer
        max_len = 0
        unique_chars = set() # keep track of non-repeated chars
        
        # loop through until right pointer equals last index of string
        while (right < len(s)):
            # if char not repeated
            if s[right] not in unique_chars:
                # add to set to keep track
                unique_chars.add(s[right])
                # compute max length of substring between current max and new substring
                max_len = max(max_len, len(unique_chars))
                right += 1 # Increase right pointer by 1
            else:
                # if char is repeated, remove from set and increase left pointer by 1
                unique_chars.remove(s[left])
                left += 1
        
        return max_len
