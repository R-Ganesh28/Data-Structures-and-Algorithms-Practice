class Solution:
    def removeDuplicateFromSortedArray(self, nums:list[int]) -> int:
        i = 1
        for j in range(1, len(nums)):
            if nums[j] != nums[i - 1]:
                nums[i] = nums[j]
                i += 1
        return i
nums = [1,1,2]
S1 = Solution()
print(S1.removeDuplicateFromSortedArray(nums))