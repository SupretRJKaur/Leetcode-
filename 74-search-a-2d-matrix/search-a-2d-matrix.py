class Solution(object):
    def searchMatrix(self, matrix, target):
        # Loop through every row
        for row in matrix:
            # Loop through every element in the current row
            for element in row:
                if element == target:
                    return True
                    
        return False