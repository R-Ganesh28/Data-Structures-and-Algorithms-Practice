class Solution:
    def uniqueNumberOfOccurences(self, arr : list[int]) -> bool:
        seen_numbers = {}
        for i in arr:
            seen_numbers[i] = seen_numbers.get(i, 0) + 1
        return len(seen_numbers.values()) == len(set(seen_numbers.values()))

arr = [1,2,2,1,1,3]
S1 = Solution()
print(S1.uniqueNumberOfOccurences(arr))
        