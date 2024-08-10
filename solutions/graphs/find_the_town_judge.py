# Leetcode No.997 https://leetcode.com/problems/find-the-town-judge/
class Solution:
    # time complexity: O(V + E)
    # space complexity: O(V)
    def findJudge(self, n: int, trust: list[list[int]]) -> int:
        potential_judges = set()
        # add all people in the town to the potential judge set
        for i in range(1, n+1):
            potential_judges.add(i)
        
        # remove all people who trust someone from the judge set
        for i in range(len(trust)):
            trusting = trust[i][0]
            if trusting in potential_judges:
                potential_judges.remove(trusting)
            
        freq = {}
        for i in range(1, n+1):
            freq[i] = 0
        # frequency dictionary: for each person how many people trust them
        for i in range(len(trust)):
            trusted = trust[i][1]
            freq[trusted] += 1
        # return a person who didn't trust anyone and was trusted by everyone else
        for potential_judge in potential_judges:
            if potential_judge in freq and freq[potential_judge] == n - 1:
                return potential_judge
        # if no judge is found
        return -1 