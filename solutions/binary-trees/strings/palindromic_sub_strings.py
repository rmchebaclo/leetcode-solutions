class Solution:
    def countSubstrings(self, s: str) -> int:
        # brute force solution
        # check every single substring
        # call helper function on substring to see if it is a palindrome
        # increment counter if it is
        # time complexity: O(n^3) where n = len(s)
        # space compelxity: O(1)
        counter = 0
        for l in range(len(s)):
            for r in range(l, len(s)):
                substring = s[l:r+1]
                if self.isPalindrome(substring):
                    counter += 1
        return counter
    
    def isPalindrome(self, substring):
        if len(substring) <= 1:
            return True
        return substring[0] == substring[-1] and self.isPalindrome(substring[1:-1])