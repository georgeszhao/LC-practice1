class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s or len(s) < 1:
            return ''
        if len(set(s)) == 1:
            return s
        left, right, max_len, n = 0, 0, 0, len(s)
        dp = [[0] * n for _ in range(n)]
        for j in range(n):
            dp[j][j] = 1
            for i in range(j):
                dp[i][j] = (s[i] == s[j]) and (j - i == 1 or dp[i + 1][j - 1])
                if dp[i][j] and max_len < j - i + 1:
                    max_len, left, right = j - i + 1, i, j
        return s[left: right + 1]

def execute() -> object:
    s = "babad"
    sol = Solution()
    print(sol.longestPalindrome(s))

if __name__ == "__main__":
    execute()

# class Solution(object):
#     def longestPalindrome(self, s):
#         """
#         :type s: str
#         :rtype: str
#         """
#         if not s or len(s) < 1:
#             return ''
#         if len(set(s)) == 1:
#             return s
#         left, right = 0, 0
#         for i in range(len(s)):
#             max_len = max(self.expandAroundCenter(s, i, i), self.expandAroundCenter(s, i, i + 1))
#             if max_len > right - left + 1:
#                 left, right = i - (max_len - 1) // 2, i + max_len // 2
#         return s[left: right + 1]
#
#     def expandAroundCenter(self, s, left, right):
#         L, R = left, right
#         while L >= 0 and R < len(s) and s[L] == s[R]:
#             L -= 1
#             R += 1
#         return R - L - 1