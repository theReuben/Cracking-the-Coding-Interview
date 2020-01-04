# Problem 70 on Leetcode, Climbing Stairs
# Runtime: 8 ms, faster than 97.55% of Python online submissions for Climbing Stairs.
# Memory Usage: 11.9 MB, less than 14.6% of Python online submissions Climbing Stairs.

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        prev2 = 0
        prev1 = 1
        total = 0
        for _ in range(n) :
            total = prev2 + prev1
            prev2 = prev1
            prev1 = total
            
        return total
