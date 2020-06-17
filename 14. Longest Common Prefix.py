class Solution:
    """
    @param strs: A list of strings
    @return: The longest common prefix
    """
    def longestCommonPrefix(self, strs):
        # write your code here
        if not strs:
            return ''
        for index, item in enumerate(zip(*strs)):
            if len(set(item))!=1:
                return strs[0][:index]
        return min(strs)

def execute() -> object:
    strs = ["ABCD","ABEF","ACEF"]
    sol = Solution()
    print(sol.longestCommonPrefix(strs))

if __name__ == "__main__":
    execute()
