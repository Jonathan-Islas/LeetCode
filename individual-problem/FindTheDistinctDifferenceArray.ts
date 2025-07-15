// CONTEXT
    // We receive a List 'nums' of length n
    // prefix and suffix reffers to elements before and after nums[i]
    // both the prefix and suffix will also refer to the unique elements with no repeated ones
    // from nums [] we have to iterate the list and substract from prefix length the suffix length 
    // and save it in a new array
        
    // REQUIREMENTS
    // Substract the suffix length from prefix length and save it in ans[i]
    // Return the new list with the values

    // ToDo
    // Iterate the list 
    // Get the Suffix and Preffix of nums[i] with unique elements
    // Save the substraction into the new array
    // return the array

function distinctDifferenceArray(nums: number[]): number[] {
    // Create our const for the length of nums and the answer
    const numsLength: number = nums.length;
    const ans: number[] = [];

    // iterate nums array
    for (let i = 0; i < numsLength; i++) {
        // get the preffix and suffix using a Set for unique elements
        let preffix: Set<number> = new Set(nums.slice(0, i+1));
        let suffix: Set<number> = new Set(nums.slice(i+1));
        // answer logic
        ans[i] = preffix.size - suffix.size;
    }
    return ans;
};
