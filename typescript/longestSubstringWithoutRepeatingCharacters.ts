// longestSubstringWithoutRepeatingCharacters.ts
function lengthOfLongestSubstring(s: string): number {

    if(s.length == 0)
        return 0
    let left = 0
    let right = 0
    let max_len = 0
    let unique_chars = new Set<string>()

    do{
        if(!unique_chars.has(s.charAt(right))){
            unique_chars.add(s.charAt(right))
            max_len = Math.max(max_len, unique_chars.size)
            right+=1
        }else{
            unique_chars.delete(s.charAt(left))
            left+=1
        }
    }while(right < s.length)
    return max_len
};
