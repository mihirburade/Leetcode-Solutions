class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """

        m=len(matrix)
        n=len(matrix[0])
        left=0
        right=m*n-1
        while left<=right:
            middle=(left+right)//2
            row=middle//n
            col=middle%n
            if matrix[row][col]==target:
                return True

            if matrix[row][col]<target:
                left=middle+1
            
            if matrix[row][col]>target:
                right=middle-1

        return False

