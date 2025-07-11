        # We receive a string s, and a pattern p
        # s will always be lowercase english letters
        # p will always be lowercase english letters and ' . ', ' * ' chars
        
        # Requirements
        # Return true if the String s follows the Pattern p, false if not
        
        # ToDo 
        # define function to determine if there's a match
        # Find a way to iterate either the string, the pattern or both if needed
        # Match the corresponding pattern char with the respective string char following
        # the . and * rules
        
        
        # Keep in mind
        # ' * ' char can be 0 or infinite number of the preceding letter
        # ' . ' char can be any letter
        
        # Matching logic?
        # check if pattern char it's a '.' or a letter
        # then check if the next char is ' * '
        # if not, current pattern char must be a 1 to 1 match with the string
        # if there's an '*', it must match current pattern char 0 o more times
        # an '*' works as a wildcard: ALWAYS RETURNS A TRUE MATCH
        
        # discussion example:
        # S = " mississippi "
        # P = " mis*is*p*. "
        # return = false
         
        
        # s = aaa, p = ab*ac*a
        # a == a? -> TRUE
        # b* -> TRUE
        # a = a? -> TRUE
        # c* -> TRUE
        # a = a -> TRUE
        
        # isMatch("aab", "c*a*b") → true
        # dos pointers: i -> indexes of s | j -> indexes of p
        # i = 0, j = 0
        # s[0] = a, p[0] = c
        # check match -> match = i < len(s) and (s[i] == p[j] or p[j] == '.')
        # check if next pattern char is an '*'
        # if p[j+1] == '*' -> we either use 1 or more times, or we ignore it (matches 0 times)
        #   don't use -> j = j+2, i stays the same
        #   we use it -> i = i+1 -> it means there's a match, so we move pointer i, pointer j stays the same
        #               use '*'                    don't use
        # return (match and checkMatch(i+1, j)) or checkMatch(i,j+2)
        
        # if p[j+1] != '*' -> we only look for 1 to 1 match, return match and move pointers on both s and p
        #   return checkMatch(i+1, j+1)

        
        # if no match, return False
        
        # EDGE CASES:
        # if i >= len(s) and j >= len(p): return True -> we reached end of both, string and pattern
        # if j >= len(p): return False -> we reached end of pattern before end of string
        # otherwise, both i and j are within bounds
        
        # a == c -> FALSE, NO MATCH
        # there's an '*' after c, so we have to match c 0 or more times
        #       *
        #   |       |
        # use    don't use
        # FALSE     TRUE
        
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        memory = {} # memoization -> key: tuple(i,j), val: True/False
        
        # helper function to be called recursively
        def checkMatch(i: int, j:int):
            # if match value is already store in memory, return value
            if (i,j) in memory:
                return memory[(i,j)]
                
            # check if we reached end of both, string and pattern
            if i >= len(s) and j >= len(p):
                return True
            
            # check if we reached end of pattern before end of string
            if j >= len(p):
                return False
            
            # check if there's match between chars. we must be within string s bounds
            # handle '.' wildcard on pattern
            chars_match = i < len(s) and (s[i] == p[j] or p[j] == '.')
            
            # check if there's an '*' after current pattern char
            if (j + 1) < len(p) and p[j+1] == '*':
                # if there is, we either ignore it (matches 0 times) or use it 1 or more times
                # if we ignore it, we move to char after '*' in pattern, while staying on the same s char
                # if we use it, it means there's a match, so we move to the next char on string s,
                # we stay on the same p char
                memory[(i,j)] = (chars_match and checkMatch(i+1, j)) or checkMatch(i,j+2) # store in memo
                return memory[(i,j)]
            # if there's no '*', we look for a 1 to 1 match
            if chars_match:
                # if there is, we move to next char on both s and p
                memory[(i,j)] = checkMatch(i+1, j+1) # store in memo
                return memory[(i,j)]
            
            # otherwise, store in memo and return False because there's no match
            memory[(i,j)] = False
            return False
            
        return checkMatch(0, 0)
