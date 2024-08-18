class Solution:
    '''
    m (rows) by n (cols) matrix
    time complexity: O(log(m*n)) or O(log(m) + log(n))
    space complexity: O(1)
    '''
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        # run binary search on the rows to find the row which the target is on
        # this is possible because rows are in sorted order as well
        l = 0
        r = len(matrix) - 1
        while l <= r:
            mid_row = (l + r) // 2
            if target > matrix[mid_row][-1]:
                l = mid_row + 1
            elif target < matrix[mid_row][0]:
                r = mid_row - 1
            else:
                break
        # if left and right pointers overlapped then a row wasn't found
        if not l <= r:
            return False
        # run binary search on the cols within the row that was found earlier
        l = 0
        r = len(matrix[mid_row])
        while l <= r:
            mid_col = (l + r) // 2
            val = matrix[mid_row][mid_col]
            if target == val:
                return True
            elif target > val:
                l = mid_col + 1
            else:
                r = mid_col - 1
        return False