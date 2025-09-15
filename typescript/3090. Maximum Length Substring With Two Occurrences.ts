function maximumLengthSubstring(s: string): number {
    const charCounts: Record<string, number> = {};
    let maxLen = 0, start = 0;

    for (let end = 0; end < s.length; end++) {
        const charEnd = s[end];

        if(!charCounts[charEnd]) {
            charCounts[charEnd] = 0;
        }
        charCounts[charEnd]++;

        while (charCounts[charEnd] > 2) {
            const charStart = s[start];
            charCounts[charStart]--;
            start++;
        }

        maxLen = Math.max(maxLen, end - start + 1);
    }

    return maxLen;
};