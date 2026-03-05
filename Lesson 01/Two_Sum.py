class Solution:
    def twoSum(self, num: list[int], target = int) -> list[int]:
        seen = {}
        for i, val in enumerate(num):
            if (target - val) in seen:
                return (seen[(target - val)], i)
            seen[val] = i
num = [2,11,7,15]
S1 = Solution()
print(S1.twoSum(num, 9))