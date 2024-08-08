class Solution:
    
    # recursive solution without memoization
    # time complexity: O(2^n), number of nodes in solution tree
    # space complexity: O(n), height of recursive stack
    def climbStairs(self, n: int) -> int:
        if n <= 1:
            return 1
        return self.climbStairs(n - 1) + self.climbStairs(n - 2)
    
    # top down dynamic programming
    # memoization to store previously calculated results
    # time complexity: O(n)
    # space complexity: O(n)
    def climbStairs(self, n: int) -> int:
        def dfs(n, cache):
            if n in cache:
                return cache[n]
            cache[n] = dfs(n-1, cache) + dfs(n-2,cache)
            return cache[n]
        return dfs(n, {0: 1, 1: 1})
    
    # bottom up dynamic programming 
    # starting from last step there is one way to get to the top: take 0 steps
    # starting from the second to last step there is one way to get to the top: take 1 step
    # using this information we can go back one step at a time and determine how long it takes from each previous step
    # so from the third to last step we can either step onto the second to last step (take 1 step) or to the last step (take 2 steps)
    # from there we have already calculated how many steps it takes to get to the top from the last and second to last step
    # so we don't need to do that again, so we sum up those values
    # now from the fourth to last step, we can either take 1 or 2 steps
    # from that third to last step or second to last step we have already calcualted how many steps we can take
    # so we can just add those up
    # this is very similar to the fibonacci sequence solution 
    # time complexity: O(n)
    # space complexity: O(1)
    def climbStairs(self, n: int) -> int:
        curr = 1
        last = 1
        for i in range(n - 1):
            tmp = curr
            curr += last
            last = tmp
        return curr