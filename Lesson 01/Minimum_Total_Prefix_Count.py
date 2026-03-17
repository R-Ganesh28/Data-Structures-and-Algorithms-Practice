class Solution:
    def minimumPrefixCount(self, arr : list[int]) -> int:
        freq = {}
        for ch in arr:
            freq[ch] = freq.get(ch, 0) + 1
        sorted_values = sorted(freq.values(), reverse = True)

        distinct = 0
        total = 0

        for i in sorted_values:
            distinct += 1
            total += distinct * i
        return total
arr = [2, 3, 1, 2, 3]
S1 = Solution()
print(S1.minimumPrefixCount(arr))