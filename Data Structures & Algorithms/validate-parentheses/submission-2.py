class Solution:
    def isValid(self, s: str) -> bool:
        pairs = { ']' : '[', '}' : '{', ')' : '('}
        stack = []

        if len(s) == 0:
            return True

        for char in s:
            if char in pairs:
                if stack and stack[-1] == pairs[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        
        return True if not stack else False