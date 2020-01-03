# Problem 152 on Leetcode, Maximum Product Subarray
# Runtime: 36 ms, faster than 90.10% of Python online submissions for Maximum Product Subarray.
# Memory Usage: 12.1 MB, less than 57.89% of Python online submissions for Maximum Product Subarray.

class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """  
        front = 0
        back = 0
        curr_max = float('-inf')
        for i in range(len(nums)):
            front = (front or 1) * nums[i]
            back = (back or 1) * nums[-i-1]
            curr_max = max(curr_max, front, back)
        return curr_max
