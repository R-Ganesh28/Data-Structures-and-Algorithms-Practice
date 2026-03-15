class Solution:
    def validParenthesis(self, s : str) -> bool:
        mapping = {
            ')' : '(',
            ']' : '[',
            '}' : '{'
        }
        stack = []
        for i in s:
            if i in mapping:
                top_element = stack.pop() if stack else '#'

                if mapping[i] != top_element:
                    return False
            else:
                stack.append(i)
        return not stack
    
s = "()"
S1 = Solution()
print(S1.validParenthesis(s))