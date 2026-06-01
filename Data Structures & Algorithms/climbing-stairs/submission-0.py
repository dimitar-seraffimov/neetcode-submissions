class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [1,2]
        if n == 1:
            return 1
        for i in range(n - 2):
             dp.append(dp[-1] + dp[-2])
        return dp[-1]