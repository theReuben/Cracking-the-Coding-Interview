# Problem 377 on Leetcode, Combination Sum IV
# Runtime: 24 ms, faster than 92.68% of Python online submissions for Combination Sum IV.
# Memory Usage: 12.2 MB, less than 66.67% of Python online submissions for Combination Sum IV.

class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # total = 0
        # q = [n for n in nums if n <= target]
        # while len(q) > 0 :
        #     print(q)
        #     for n in nums :
        #         if q[0] + n < target :
        #             q.append(q[0] + n)
        #         elif q[0] + n == target :
        #             total += 1
        #         elif q[0] == target :
        #             total += 1
        #             break
        #     q.pop(0)
        # return total
        
        # This solution is slower, but uses less storage
        # q = [n for n in nums if n <= target]
        # q.sort()
        # mem = [-1] * (target+1)
        # mem[target] = 1
        # while len(q) > 0 :
        #     print(q)
        #     breaking = False
        #     local = 0
        #     for n in nums :
        #         if q[-1] + n <= target :
        #             if mem[q[-1] + n] >= 0 :
        #                 local += mem[q[-1] + n]
        #             else :
        #                 q.append(q[-1] + n)
        #                 breaking = True
        #         elif q[-1] == target :
        #             local = 1
        #     if breaking : continue
        #     mem[q[-1]] = local
        #     q.pop()
        # return sum([mem[i] for i in nums if i <= target])
        
        dp = [1] + [0] * target
        for i in range(1, target + 1):
            dp[i] = sum([dp[i - n] for n in nums if i >= n])
        return dp[-1]
