class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return []
        up, down = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1
        ans, direction = [], 0
        while up <= down and left <= right:
            if direction == 0:
                for j in range(left, right + 1):
                    ans.append(matrix[up][j])
                up += 1
            if direction == 1:
                for i in range(up, down + 1):
                    ans.append(matrix[i][right])
                right -= 1
            if direction == 2:
                for j in range(right, left - 1, -1):
                    ans.append(matrix[down][j])
                down -= 1
            if direction == 3:
                for i in range(down, up - 1, -1):
                    ans.append(matrix[i][left])
                left += 1
            direction = (direction + 1) % 4
        return ans

def execute() -> object:
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    sol = Solution()
    print(sol.spiralOrder(matrix))

if __name__ == "__main__":
    execute()

