# Problem 238 on Leetcode, Product of Array Except Self
# Runtime: 104 ms, faster than 74.46% of Python online submissions for Product of Array Except Self.
# Memory Usage: 18.4 MB, less than 78.57% of Python online submissions for Product of Array Except Self.

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        lng = len(nums)
        out = [1 for _ in range(lng)]
        
        for i in range(1, lng) :
            out[i] *= nums[i-1] * out[i-1]
        
        back = 1
        for i in range(lng-2, -1, -1) :
            back *= nums[i+1]
            out[i] *= back
            
        return out
