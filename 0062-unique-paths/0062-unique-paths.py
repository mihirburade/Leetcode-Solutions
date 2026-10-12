class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        mat=[[1]*n for _ in range(m)]

        for i in range(1,m):
            for j in range(1,n):
                mat[i][j]=mat[i-1][j]+mat[i][j-1]

        return mat[m-1][n-1]
        
