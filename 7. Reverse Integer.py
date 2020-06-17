class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return 0
        ans, sign = 0, 1 if x > 0 else -1
        x = abs(x)
        while x:
            ans = ans * 10 + x % 10
            x //= 10
        ans *= sign
        return ans if -(1 << 31) <= ans <= (1 << 31) - 1 else 0

def execute() -> object:
    x = -63847412
    sol = Solution()
    print(sol.reverse(x))

if __name__ == "__main__":
    execute()

