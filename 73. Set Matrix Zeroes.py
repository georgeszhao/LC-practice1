class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        if not matrix:
            return
        m, n = len(matrix), len(matrix[0])
        x, y = set(), set()
        for i in range(m):
            for j in range(n):
                if not matrix[i][j]:
                    x.add(i); y.add(j)
        for i in x:
            for j in range(n):
                matrix[i][j] = 0
        for j in y:
            for i in range(m):
                matrix[i][j] = 0
        return matrix

def execute():
    matrix = [[0,1,0],[0,0,1],[1,1,1]]
    sol = Solution()
    print(sol.setZeroes(matrix))

if __name__ == "__main__":
    execute()

# class Solution(object):
#     def setZeroes(self, matrix):
#         """
#         :type matrix: List[List[int]]
#         :rtype: None Do not return anything, modify matrix in-place instead.
#         """
#         if not matrix:
#             return
#         m, n = len(matrix), len(matrix[0])
#         row, col = [False] * m, [False] * n
#         for i in range(m):
#             for j in range(n):
#                 if not matrix[i][j]:
#                     row[i], col[j] = True, True
#         for i in range(m):
#             for j in range(n):
#                 if row[i] or col[j]:
#                     matrix[i][j] = 0
#         return matrix