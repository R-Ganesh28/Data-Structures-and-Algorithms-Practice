class Solution:
    def removeElement(self, nums:list[int], val : int) -> int:
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k
nums = [3, 2, 2, 3]
val = 3
S1 = Solution()
print(S1.removeElement(nums, val))