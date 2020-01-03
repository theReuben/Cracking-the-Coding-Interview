# Problem 153 on Leetcode, Find Minimum in Rotated Array
# Runtime: 16 ms, faster than 99.41% of Python online submissions for Find Minimum in Rotated Array.
# Memory Usage: 12.0 MB, less than 57.14% of Python online submissions for Find Minimum in Rotated Array.

class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) is 1 or nums[0] < nums[-1]: return nums[0]
        if len(nums) is 2 : return min(nums[0], nums[1])
        
        minn = 0
        maxx = len(nums)-1
        check = (minn+maxx)//2
        
        while True :
            if nums[check] < nums[check-1] and check > 0 :
                return nums[check]
            if nums[check] > nums[check+1] and check < len(nums)-1:
                return nums[check+1]

            if nums[check] > nums[0] :
                minn = check
            elif nums[check] < nums[0] :
                maxx = check
            check = (minn+maxx)//2
