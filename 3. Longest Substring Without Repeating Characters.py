class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans, start, dict = 0, 0, {}
        for index, value in enumerate(s):
            if value in dict and dict[value] >= start:
                start = dict[value] + 1
            else:
                ans = max(ans, index - start + 1)
            dict[value] = index
        return ans

def execute() -> object:
    s = "abcabcbb"
    sol = Solution()
    print(sol.lengthOfLongestSubstring(s))

if __name__ == "__main__":
    execute()

