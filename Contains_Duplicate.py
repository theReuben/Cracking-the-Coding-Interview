# Problem 217 on Leetcode, Contains Duplicate
# Runtime: 100 ms, faster than 92.15% of Python online submissions for Contains Duplicate.
# Memory Usage: 17.2 MB, less than 55.55% of Python online submissions for Contains Duplicate.

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        dup = False
        stored = set()
        
        for n in nums :
            if n in stored :
                dup = True
                break
            stored.add(n)
            
        return dup
