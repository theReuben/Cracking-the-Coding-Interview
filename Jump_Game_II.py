# Problem 45 on Leetcode, Jump Game II
# Runtime: 68 ms, faster than 98.65% of Python online submissions for Jump Game II.
# Memory Usage: 13.8 MB, less than 16.67% of Python online submissions for Jump Game II.

class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        start = 0
        stop = 0
        step = 0
        while stop < len(nums)-1 :
            start, stop, step = stop+1, max([nums[i] + i for i in range(start, stop+1)]), step+1
        return step
