class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if not n:
            return []
        ans = []
        self.helper(n, n, '', ans)
        return ans

    def helper(self, left, right, item, ans):
        if left > right:
            return
        if not left and not right:
            ans.append(item)
        if left:
            self.helper(left - 1, right, item + '(', ans)
        if right:
            self.helper(left, right - 1, item + ')', ans)

def execute() -> object:
    n = 7
    sol = Solution()
    print(sol.generateParenthesis(n))

if __name__ == "__main__":
    execute()