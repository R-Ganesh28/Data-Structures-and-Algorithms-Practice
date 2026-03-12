class Solution:
    def twoSumInputArrayIsSorted(self, nums:list[int], target = int) -> list[int]:
        left = 0
        right = len(nums) - 1
        while left < right:
            Total = nums[left] + nums[right]
            if target == Total:
                return [left + 1, right + 1]
            elif target < Total:
                right -= 1
            else:
                left += 1
        return[]
nums = [2,7,11,15]
target = 9
S1 =  Solution()
print(S1.twoSumInputArrayIsSorted(nums, target))