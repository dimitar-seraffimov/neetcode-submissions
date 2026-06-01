class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # minimal constraints 2 <= cost.length <= 100
        n = len(cost)

        # prev1 is the cost to reach the step 1 steps behind current
        prev1 = 0
        prev2 = 0         

        # iterate to the 'top' which is index n
        for i in range(2, n + 1):
        # cost to reach current step is:
            # min(cost to reach i-1 + cost of i-1, cost to reach i-2 + cost of i-2)
            current = min(prev1 + cost[i - 1], prev2 + cost[i - 2])
            
            # shift variables for next iteration
            prev2 = prev1
            prev1 = current

        return prev1  
