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
        
        paren = {"(" : ")", "[" : "]", "{" : "}"}
        
        chars = [s[i] for i in range(len(s))]
        
        op = [key for key, val in paren.items()]
        cl = [val for key, val in paren.items()]
        
        for c in chars:
            if chars[0] in cl:
                return False
            elif chars[-1] in op:
                return False
            elif c in op:
                stack.append(paren[c])
            elif len(stack) > 0 and c == stack[-1]:
                stack.pop()
            else:
                return False
            
        if len(stack) == 0:
            return True
        else:
            return False
