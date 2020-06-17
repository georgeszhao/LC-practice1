class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        ans, index = [[0] * n for _ in range(n)], 1
        up, down, left, right = 0, n - 1, 0, n - 1
        while index <= n * n:
            for j in range(left, right + 1):
                ans[up][j] = index
                index += 1
            up += 1
            for i in range(up, down + 1):
                ans[i][right] = index
                index += 1
            right -= 1
            for j in range(right, left - 1, -1):
                ans[down][j] = index
                index += 1
            down -= 1
            for i in range(down, up - 1, -1):
                ans[i][left] = index
                index += 1
            left += 1
        return ans

def execute() -> object:
    n = 2
    sol = Solution()
    print(sol.generateMatrix(n))

if __name__ == "__main__":
    execute()

