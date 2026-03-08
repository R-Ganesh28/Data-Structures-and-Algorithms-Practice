class Solution:
    def validAnagram (self, s : str, t : str) -> bool:
        if len(s) != len(t):
            return False
        else:
            freq = {}
            for ch in s:
                freq[ch] = freq.get(ch, 0) + 1
            for ch in t:
                if ch not in freq or freq[ch] == 0:
                    return False
                freq[ch] -= 1
            else:
                return True
s = "carrace"
t = "racecar"
S1 = Solution()
print(S1.validAnagram(s,t))