class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle:
            return 0
        m, n = len(haystack), len(needle)
        for i in range(m - n + 1):
            if haystack[i] != needle[0]:
                continue
            if haystack[i: i + n] == needle:
                return i
        return -1
    
def execute() -> object:
    haystack, needle = "hello", "ll"
    sol = Solution()
    print(sol.strStr(haystack, needle))

if __name__ == "__main__":
    execute()
