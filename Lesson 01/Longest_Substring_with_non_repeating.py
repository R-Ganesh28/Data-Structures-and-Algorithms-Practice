class Solution:
    def longest_substring_with_non_repeating(self, s : str) -> int:
        seen = {}
        left = 0
        maxlength = 0
        for right in range(len(s)):
            if s[right] in seen:
                left = max(left, seen[s[right]] + 1)
            seen[s[right]] = right
            maxlength = max(maxlength, right - left + 1)
        return maxlength
    
s = "abcabcbb"
S1 = Solution()
print(S1.longest_substring_with_non_repeating(s))