class Solution:
    def minimumSubarrayLengthWithKDistinct(self, arr : list[int], k = int) -> int:
        from collections import defaultdict

        freq = defaultdict(int)
        distinct = 0
        minlen = float('inf')
        left = 0

        for right in range(len(arr)):
            if freq[arr[right]] == 0:
                distinct += 1
            freq[arr[right]] += 1

            while distinct > k:
                freq[arr[left]] -= 1
                if freq[arr[left]] == 0:
                    distinct -= 1
                left += 1

            while distinct == k:
                minlen = min(minlen, right - left + 1)

                freq[arr[left]] -= 1
                if freq[arr[left]] == 0:
                    distinct -= 1
                left += 1
        return (minlen if minlen != float('inf') else -1)
arr = [1, 2, 1, 2, 3]
k = 2
S1 = Solution()
print(S1.minimumSubarrayLengthWithKDistinct(arr, k))