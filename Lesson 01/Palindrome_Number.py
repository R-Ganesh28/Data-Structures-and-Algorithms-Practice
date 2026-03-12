class Solution:
    def palindromeNumber(self, n:int) -> bool:
        if n < 0:
            return False
        else:
            temp = n
            reverse = 0
            while temp > 0:
                last_digit = temp % 10
                reverse = (reverse * 10) + last_digit
                temp = temp // 10
            return n == reverse
n = -121
S1 = Solution()
print(S1.palindromeNumber(n))