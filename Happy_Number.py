
# Problem 202 on Leetcode, Happy Number
# Runtime: 12 ms, faster than 97.77% of Python online submissions for Happy Number.
# Memory Usage: 11.5 MB, less than 100.00% of Python online submissions for Happy Number.

class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        num = [str(n)[i] for i in range(len(str(n)))]
        summ = 0
        memory = []
        while summ is not 1:
            summ = 0
            for j in num:
                summ += int(j)**2
            if summ in memory:
                return False
            memory.append(summ)
            number = str(summ)
            num = [number[i] for i in range(len(number))]
        return True
