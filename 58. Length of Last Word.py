class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.strip()
        if not s:
            return 0
        ans = 0
        for i in s[::-1]:
            if i == ' ':
                return ans
            else:
                ans += 1
        return ans



def execute() -> object:
    s = "Hello World"
    sol = Solution()
    print(sol.lengthOfLastWord(s))

if __name__ == "__main__":
    execute()
