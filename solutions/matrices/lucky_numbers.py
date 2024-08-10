# Leetcode No.1380 https://leetcode.com/problems/lucky-numbers-in-a-matrix/description/
class Solution:
    # time complexity: O(m * n), m = len(matrix), n = len(matrix[i])
    # space complexity: O(m)
    def luckyNumbers (self, matrix: list[list[int]]) -> list[int]:
        rows, cols = len(matrix), len(matrix[0])
        row_mins = set()
        
        # add minimum of each row to a hashset
        for r in range(rows):
            row_mins.add(min(matrix[r]))

        lucky_numbers = []

        # get maximum of each column and add it to lucky numbers if it was a row minimum
        # this works because all values in the input matrix are unique
        for c in range(cols):
            max_val = matrix[0][c]
            for r in range(rows):
                max_val = max(max_val, matrix[r][c])
            if max_val in row_mins:
                lucky_numbers.append(max_val)
        return lucky_numbers
    
    # solution can be improved to O(1) space after realizing the amount of lucky numbers is capped at 1
    # take this example
    # 3  7   8
    # 9  11  13
    # 15 16  17
    # so by looking at this matrix we know that 15 is a lucky number because it is the minimum in its row and max in its column
    # that means by definiton nothing in its row or column can be a lucky number, so lets cross those off
    # X  7   8
    # X  11  13
    # 15 X   X
    # trying another number not in its row or col to be lucky, lets take 11
    # in order for 11 to be lucky it has to be smaller than anything in its row
    # however there is an additional constraint on this based on 15 being lucky
    # because 11 is in the same row as a number that was in the same column as 15 
    # (this number must be smaller than 15 since it is in the same column as 15 was lucky)
    # it also must be less than 15 to qualifty being lucky since it has to be the smallest in its row
    # at the same time 11 is in the same column as a number that was in the same row as 15
    # by definiton of a lucky number 11 must be the largest in its column so it must be larger than 15
    # this is a contradiction as 11 can't be greater than and less than 15
    # this contradicition arises for every other number in the matrix if you apply the same logic
    # so 11
    def luckyNumbers (self, matrix: list[list[int]]) -> list[int]:
        rows, cols = len(matrix), len(matrix[0])
        row_mins = set()
        
        # add minimum of each row to a hashset
        for r in range(rows):
            row_mins.add(min(matrix[r]))
        # get maximum of each column and add it to lucky numbers if it was a row minimum
        # this works because all values are unique in the input matrix
        for c in range(cols):
            max_val = matrix[0][c]
            for r in range(rows):
                max_val = max(max_val, matrix[r][c])
            if max_val in row_mins:
                # instantly return if lucky number is found since there can be 1 at most
                return [max_val]
        # if no lucky numbers are found
        return []
