class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        ROMAN ={'I':1, 'V':5, 'X':10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        if s == "":
            return 0
        index = len(s) - 2
        sum = ROMAN[s[-1]]
        while index >= 0:
            if ROMAN[s[index]] < ROMAN[s[index+1]]:
                sum -= ROMAN[s[index]]
            else:
                sum += ROMAN[s[index]]
            index -= 1
        return sum

def execute():
    s = "DIX"
    sol = Solution()
    print(sol.romanToInt(s))


if __name__ == "__main__":
    execute()



