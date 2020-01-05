# Problem 91 on Leetcode, Decode Ways
# Runtime: 16 ms, faster than 92.19% of Python online submissions for Decode Ways.
# Memory Usage: 11.8 MB, less than 52.17% of Python online submissions for Decode Ways.

class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 1 : return int(int(s[0]) != 0)
        if int(s[0]) == 0 : return 0
        dp = [0] * len(s)
        if int(s[0]) : dp[0] = 1
        dp[1] = dp[0]
        if int(s[1]) :
            if int(s[0]) == 1 or (int(s[0]) == 2 and int(s[1]) <= 6) : dp[1] += 1
        elif int(s[0]) > 2 : return 0
        for i in range(2, len(s)) :
            if int(s[i]) > 0 :
                dp[i] = dp[i-1]
            if int(s[i-1]) == 1 or (int(s[i-1]) == 2 and int(s[i]) <= 6) :
                dp[i] += dp[i-2]
        print(dp)
        return dp[-1]
                
