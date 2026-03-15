class Solution:
    def singleElementInASortedArray(self, nums : list[int]) -> int:
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = (left + right)//2
            if mid % 2 == 1:
                mid -= 1
            if nums[mid] != nums[mid + 1]:
                right = mid 
            else:
                left = mid + 2
        return nums[left]
nums = [1,1,2,3,3,4,4,8,8]
S1 = Solution()
print(S1.singleElementInASortedArray(nums))
