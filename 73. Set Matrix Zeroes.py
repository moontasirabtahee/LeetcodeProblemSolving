class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        r = len(matrix)
        c = len(matrix[0])


        frz = any(matrix[i][0] == 0 for i in range(r))
        fcz = any(matrix[0][i] == 0 for i in range(c))

        for i in range(1,r):
            for j in range(1, len(c)):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        for i in range(1, r):
            for j in range(1, c):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        if frz:
            for j in range(r):
                matrix[j][0] = 0

        if fcz:
            for i in range(c):
                matrix[0][i] = 0

# Example usage:
sol = Solution()
matrix = [[1,0,3]]

sol.setZeroes(matrix)
print(matrix)  # Output: [[0, 0]]
