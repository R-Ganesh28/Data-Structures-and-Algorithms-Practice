class Solution:
    def MajorityElement (self, nums: list) -> int:
        freq = {}
        for ch in nums:
            freq[ch] = freq.get(ch, 0) + 1
        max_value = max_frequency = 0
        for key, value in freq.items():
            if value > max_value:
                max_value = value
                max_frequency = key
        print(max_frequency)

nums = [3, 2, 3]
S1 = Solution()
S1.MajorityElement(nums)