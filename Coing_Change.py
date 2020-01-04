# Problem 322 on Leetcode, Coin Change
# Runtime: 148 ms, faster than 99.15% of Python online submissions for Coin Change.
# Memory Usage: 11.9 MB, less than 75.00% of Python online submissions for Coin Change.

class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        coins.sort(reverse=True)
        lenc, self.res = len(coins), 2**31-1

        def dfs(pt, rem, count):
            if not rem:
                self.res = min(self.res, count)
            for i in range(pt, lenc):
                if coins[i] <= rem < coins[i] * (self.res-count): 
                    dfs(i, rem-coins[i], count+1)

        for i in range(lenc):
            dfs(i, amount, 0)
        return self.res if self.res < 2**31-1 else -1
