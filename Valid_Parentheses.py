# Problem 20 on Leetcode, Valid Parentheses
# Runtime: 12 ms, faster than 96.35% of Python online submissions for Valid Parentheses.
# Memory Usage: 12 MB, less than 5.04% of Python online submissions for Valid Parentheses.

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        stack = []
        
        chars = [s[i] for i in range(len(s))]
        
        for c in chars:
            if chars[0] in [")", "]", "}"]:
                return False
            elif chars[-1] in ["(", "[", "{"]:
                return False
            elif c == "(":
                stack.append(")")
            elif c == "{":
                stack.append("}")
            elif c == "[":
                stack.append("]")
            elif len(stack) > 0 and c == stack[-1]:
                stack.pop()
            else:
                return False
            
        if len(stack) == 0:
            return True
        else:
            return False
