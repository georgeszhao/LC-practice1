class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if x == 1 or n == 0:
            return 1
        if x == 0 and n > 0:
            return 0
        if x == 0 and n < 0:
            return 'Inf'
        ans, power = 1.0, abs(n)
        while power:
            if power % 2:
                ans *= x
            x *= x
            power //= 2
        return ans

def execute() -> object:
    x, n = 2.00000, 5
    sol = Solution()
    print(sol.myPow(x, n))


if __name__ == "__main__":
    execute()

