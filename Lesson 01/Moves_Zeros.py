class Solution:
    def movesZeros (self, nums:list[int]) -> list:
        left = 0
        for right in range(1, len(nums)):
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
        return nums
nums = [0, 1, 0, 3, 0, 12]
S1 = Solution()
print(S1.movesZeros(nums))