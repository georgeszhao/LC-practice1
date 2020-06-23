class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        ans, m, n, carry = '', len(a) - 1, len(b) - 1, 0
        while m >= 0 or n >= 0:
            x = int(a[m]) if m >= 0 else 0
            y = int(b[n]) if n >= 0 else 0
            carry, digit = (x + y + carry) // 2, (x + y + carry) % 2
            if digit:
                ans = '1' + ans
            else:
                ans = '0' + ans
            m -= 1
            n -= 1
        return ans if carry == 0 else '1' + ans

def execute() -> object:
    a, b = "11", "1"
    sol = Solution()
    print(sol.addBinary(a, b))

if __name__ == "__main__":
    execute()

