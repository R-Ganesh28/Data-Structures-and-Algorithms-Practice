class Solution:
    def rotateArray(self, nums:list[int], k:int) -> list[int]:
        k %= len(nums)

        def reverse(left, right):
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
        
        reverse(0, len(nums) - 1)
        reverse(0, k - 1)
        reverse(k, len(nums) - 1)
        return nums
nums = [1, 2, 3, 4, 5, 6, 7]
k = 3
S1 = Solution()
print(S1.rotateArray(nums,k))