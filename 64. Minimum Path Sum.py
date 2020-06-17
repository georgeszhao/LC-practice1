class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if not i and j:
                    grid[0][j] += grid[0][j-1]
                if i and not j:
                    grid[i][0] += grid[i-1][0]
                if i and j:
                    grid[i][j] += min(grid[i-1][j], grid[i][j-1])
        return grid[-1][-1]


def execute() -> object:
    grid = [[1,3,1],[1,5,1],[4,2,1]]
    sol = Solution()
    print(sol.minPathSum(grid))


if __name__ == "__main__":
    execute()
