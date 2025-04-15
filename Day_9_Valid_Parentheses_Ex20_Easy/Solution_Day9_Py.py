class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        mapping = {')': '(', '}': '{', ']': '['}

        for char in s:
            if char in mapping.values():
                stack.append(char)
            elif char in mapping:
                if not stack or stack[-1] != mapping[char]:
                    return False
                stack.pop()
            else:
                return False  # invalid character

        return not stack
"""
if __name__ == "__main__":
    s = Solution()
    print(s.isValid("()"))        
    print(s.isValid("()[]{}"))    
    print(s.isValid("(]"))        
    print(s.isValid("([)]"))      
    print(s.isValid("{[]}"))      
"""
