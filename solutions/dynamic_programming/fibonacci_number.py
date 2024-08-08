class Solution:
    # recurisve solution
    # top down without memoization
    # break down problem with recursive step until we get to n = 0 or 1 because we know the value of those
    # fill values back to the top of the tree until we reach a solution for n
    # inefficient because we have to calculate same sequence of values multiple times
    # time complexity: O(2^n), that is the number of nodes in the solution tree
    # space complexity: O(n), height of the recursive stack
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        return self.fib(n-1) + self.fib(n-2)
    # bottom up solution
    # we can start from the known numbers in the sequence (0 and 1) and work up from there
    # calculate the next number in the sequence by adding up 2 previous numbers
    # before calculating make sure to store the current number to have access for next calculation
    # time complexity: O(n)
    # space complexity: O(1)
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        last = 0
        curr = 1
        for i in range(n - 1):
            tmp = curr
            curr += last
            last = tmp
        return curr
    
    # top down solution
    # use memoization to store previously calculated values and avoid redundancy
    # time complexity: O(n)
    # space complexity: O(n)
    def fib(self, n: int) -> int:
        def dp(n, cache):
            if n in cache:
                return cache[n]
            cache[n] = dp(n-2, cache) + dp(n-1, cache)
            return cache[n]
        return dp(n, {0: 0, 1: 1})