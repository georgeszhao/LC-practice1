import sys
class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        ans = 0
        sign = 1 if dividend ^ divisor >= 0 else -1
        divd, divr = abs(dividend), abs(divisor)
        while divd >= divr:
            temp, i = divr, 1
            while divd >= temp:
                divd -= temp
                ans += i
                i <<= 1
                temp <<= 1
        return min(max(ans * sign, -sys.maxsize), sys.maxsize)

def execute() -> object:
    dividend = 10
    divisor = 3
    sol = Solution()
    print(sol.divide(dividend, divisor))

if __name__ == "__main__":
    execute()
