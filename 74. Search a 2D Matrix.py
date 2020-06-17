class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or len(matrix)==0 or len(matrix[0])==0:
            return False
        m, n, i= len(matrix), len(matrix[0]), 0
        for row in matrix:
            if row[n-1] < target:
                i+=1
            else:
                break
        return (i<=m-1) and target in matrix[i]

def execute():
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
    target= 15
    sol = Solution()
    print(sol.searchMatrix(matrix, target))

if __name__ == "__main__":
    execute()
