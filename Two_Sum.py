# Problem 1 on Leetcode
# Runtime: 32 ms, faster than 91.06% of Python online submissions for Two Sum.
# Memory Usage: 13.4 MB, less than 11.96% of Python online submissions for Two Sum.
# The solution runs in O(n) time, with O(n) storage

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        diff_dict = {}
        diff_set = set()
        for i in range(len(nums)) :
            diff = target - nums[i]
            if diff in diff_set : 
                return [i, diff_dict[target - diff]]
            else :
                diff_dict[diff] = i
                diff_set.add(nums[i])
            
            
        
