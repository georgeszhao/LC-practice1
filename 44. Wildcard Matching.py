class Solution(object):
    def isMatch(self, s, p):
        """ similar to 10
        :type s: str
        :type p: str
        :rtype: bool
        """
        if not s and not p:
            return True
        if s and not p:
            return False
        m, n = len(s), len(p)
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True
        for j in range(1, n + 1):
            if p[j - 1] == '*':
                dp[0][j] |= dp[0][j - 1]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s[i - 1] == p[j - 1] or p[j - 1] == '?':
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j - 1] == '*':
                    dp[i][j] = dp[i - 1][j - 1] or dp[i - 1][j] or dp[i][j - 1]
        return dp[-1][-1]

def execute() -> object:
    s = "adceb"
    p = "*a*b"
    sol = Solution()
    print(sol.isMatch(s, p))

if __name__ == "__main__":
    execute()