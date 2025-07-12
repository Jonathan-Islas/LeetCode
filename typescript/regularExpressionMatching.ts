// regularExpressionMatching.ts
function isMatch(s: string, p: string): boolean {
    const memory = new Map<string, boolean>() // memoization -> key: str(i) + str(), val: True/False

    // helper function to be called recursively
    function checkMatch(i: number, j: number) {
        // concat pointers i and j into a string to serve as key
        const key: string = i + '' + j;

        // if match value is already store in memory, return value
        if (memory.has(key)) {
            return memory.get(key);
        }

        // check if we reached end of both, string and pattern
        if (j === p.length) {
            return i === s.length;
        }

        // check if there's match between chars. we must be within string s bounds handle '.' wildcard on pattern
        const charsMatch = (i < s.length && (s[i] === p[j] || p[j] === '.'));

        let matchingResult;
        // check if there's an '*' after current pattern char
        if ((j + 1) < p.length && p[j + 1] === '*') {
            // if there is, we either ignore it (matches 0 times) or use it 1 or more times
            // if we ignore it, we move to char after '*' in p, while staying on the same s char
            // if we use it, it means there's a match, so we move to the next char on string s,
            // we stay on the same p char
            matchingResult = (charsMatch && checkMatch(i + 1, j)) || checkMatch(i, j + 2);
        } else {
            // if there's no '*', we look for a 1 to 1 match. if there is, we move to next char on both s and p
            matchingResult = charsMatch && checkMatch(i + 1, j + 1);
        }

        memory.set(key, matchingResult); // store matching result in memo
        return matchingResult; // return matching result
    }
    return checkMatch(0, 0);
};
