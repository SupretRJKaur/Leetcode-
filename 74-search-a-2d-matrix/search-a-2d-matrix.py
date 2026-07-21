class Solution(object):
    def searchMatrix(self, matrix, target):
        for row in matrix:
            for element in row:
                if element == target:
                    return True
        return False