class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        pars = [None]
        dict = {')': '(',
                '}': '{',
                ']': '['}
        for c in s:
            if c in dict and dict[c] == pars[-1]:
                pars.pop()
            else:
                pars.append(c)
        return len(pars) == 1

def execute() -> object:
    s= "()"
    sol = Solution()
    print(sol.isValid(s))


if __name__ == "__main__":
    execute()
