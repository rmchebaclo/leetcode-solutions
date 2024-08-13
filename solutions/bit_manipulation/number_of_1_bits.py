class Solution:
    # time complexity: O(logn), dividing number in half every operation 
    # space complexity: O(1)
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n > 0:
            if n & 1 == 1:
                count += 1
            n = n >> 1
        return count