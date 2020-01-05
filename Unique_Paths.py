# Problem 62 on Leetcode, Unique Paths
# Runtime: 16 ms, faster than 79.54% of Python online submissions for Unique Paths.
# Memory Usage: 11.8 MB, less than 34.48% of Python online submissions for Unique Paths.

# O(m * n)
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [[0 for _ in range(m)] for _ in range(n)]
        for i in range(n) : dp[i][0] = 1
        for j in range(m) : dp[0][j] = 1
        for i in range(1, n) :
            for j in range(1, m) :
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        print(dp)
        return dp[-1][-1]
      
