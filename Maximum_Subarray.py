# Problem 53 on Leetcode, Maximum Subarray
# Runtime: 44 ms, faster than 95.92% of Python online submissions for Maximum Subarray.
# Memory Usage: 12.3 MB, less than 47.43% of Python online submissions for Maximum Subarray.

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        long_sum = 0
        curr_sum = 0
        max_val = nums[0]
        
        for n in nums :
            long_sum += n
            curr_sum += n
            max_val = max(max_val, long_sum, curr_sum)
            if n < 0 :
                long_sum = max(long_sum, curr_sum)
                curr_sum = 0
        
        return max_val
             
