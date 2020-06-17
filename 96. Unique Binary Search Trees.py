class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        if not n or n < 1:
            return 0
        dp = [0] * (n+1)
        dp[0], dp[1] = 1, 1
        for i in range(2, n+1):
            for j in range(i):
                dp[i] += dp[j] * dp[i-1-j]
        return dp[-1]

def execute():
    n = 3
    sol = Solution()
    print(sol.numTrees(n))


if __name__ == "__main__":
    execute()


