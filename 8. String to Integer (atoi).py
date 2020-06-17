class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        s = str.strip()
        if not s:
            return 0
        ans, i, sign, max_int = 0, 0, 1, (1 << 31) - 1
        if s[i] == '+':
            i += 1
        elif s[i] == '-':
            i += 1
            sign = -1
        while i < len(s) and '0' <= s[i] <= '9':
            ans = ans * 10 + int(s[i])
            i += 1
            if ans > max_int:
                break
        ans *= sign
        if ans >= max_int:
            return max_int
        if ans <= -(max_int + 1):
            return -(max_int + 1)
        return ans

def execute():
    str = "4193 with words"
    sol = Solution()
    print(sol.myAtoi(str))

if __name__ == "__main__":
    execute()