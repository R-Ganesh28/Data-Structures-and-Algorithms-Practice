class Solution:
    def firstLetterToAppearTwice(self, s : str) -> str:
        seen_characters = {}
        for i in s:
            if i in seen_characters:
                return i
            seen_characters[i] = i
s = "abccbaacz"
S1 = Solution()
print(S1.firstLetterToAppearTwice(s))