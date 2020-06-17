class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        left, right = 0, x + 1
        while left < right:
            mid = left + (right - left) // 2
            if mid * mid == x:
                return mid
            if mid * mid > x:
                right = mid
            else:
                left = mid + 1
        return left - 1

def execute() -> object:
    x = 2147483647
    sol = Solution()
    print(sol.mySqrt(x))

if __name__ == "__main__":
    execute()


# class Solution:
#     def mySqrt(self, x: int) -> int:
#         y = x
#         while y * y > x:
#             y = (y + x // y) // 2
#         return y
