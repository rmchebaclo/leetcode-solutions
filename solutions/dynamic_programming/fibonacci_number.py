class Solution:
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