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
    
    # optimal solution
    # for each character in s treat it like the middle of the substring and expand around it
    # stop expanding when left or right pointer goes out of bounds
    # for odd length palindromes start with left and pointer equal to eachother then expand around it
    # for even length palindromes start with right pointer being 1 greater than left
    # time complexity: O(n^2)
    # space complexity: O(1)
    def countSubstrings(self, s: str) -> int:
        res = 0
        i = 0
        for i in range(len(s)):
            res += self.countPalindromes(s, i, i)
            res += self.countPalindromes(s, i, i + 1)
        return res
    
    def countPalindromes(self, s, l, r):
        counter = 0
        while l >= 0 and r < len(s) and s[l] == s[r]:
            counter += 1
            l -= 1
            r += 1
        return counter