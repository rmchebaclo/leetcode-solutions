class Solution:
    # brute force solution trying all possible paths starting from either 0th or 1st index
    # return path with smallest cost
    # time complexity: O(2^n)
    # space complexity: O(n)
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        return min(self.total_cost(0, cost), self.total_cost(1,cost))
        
    def total_cost(self, start, cost):
        if start >= len(cost) - 2:
            return cost[start]
        return cost[start] + min(self.total_cost(start + 1, cost), self.total_cost(start + 2, cost))