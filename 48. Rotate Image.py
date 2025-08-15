class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """

        # transpose the matrix
        m = len(matrix)
        n = len(matrix[0])
        for i in range(m):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]


        # reverse each row
        for i in range(m):
            matrix[i].reverse()

