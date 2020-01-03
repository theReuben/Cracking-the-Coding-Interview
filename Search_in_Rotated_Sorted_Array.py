# Problem 33 on Leetcode, Search in Rotated Sorted Array
# Runtime: 20 ms, faster than 96.75% of Python online submissions for Search in Rotated Sorted Array.
# Memory Usage: 12.0 MB, less than 36.74% of Python online submissions for Search in Rotated Sorted Array.

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left, right = 0, len(nums)-1
        
        while left <= right :
            check = (left + right) // 2
            print(check)
            if nums[check] == target : return check
            
            elif nums[left] <= nums[check]:
                if nums[left] <= target <= nums[check]: right = check 
                else: left = check + 1
            else:
                if nums[check] <= target <= nums[right]: left = check + 1
                else: right = check 
        
        return -1
