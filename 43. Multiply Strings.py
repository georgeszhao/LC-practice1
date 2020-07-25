class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        ans, m, n = 0, len(num1), len(num2)
        for i in range(m):
            a = int(num1[m - 1 - i])
            for j in range(n):
                b = int(num2[n - 1 - j])
                ans += a * b * 10 ** (i + j)
        return str(ans)

def execute() -> object:
    num1, num2 = '11', '23'
    sol = Solution()
    print(sol.multiply(num1, num2))


if __name__ == "__main__":
    execute()