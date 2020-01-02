# Problem 121 on Leetcode, Best Time to Buy and Sell Stock
# Runtime: 48 ms, faster than 70.61% of Python online submissions for Best Time to Buy and Sell Stock.
# Memory Usage: 12.5 MB, less than 59.63% of Python online submissions for Best Time to Buy and Sell Stock.

import sys

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_diff = 0
        curr_min = sys.maxint
        curr_max = -sys.maxint + 1
        
        for p in prices :
            if p < curr_min : 
                curr_min = p
                curr_max = -sys.maxint + 1
            elif p > curr_max : curr_max = p
            max_diff = max(max_diff, curr_max - curr_min) 
        
        return max_diff
            
        
