### Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __repr__(self):
        return "{}".format(self.val)

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        return self.dfs(1, n) if n else []

    def dfs(self, start, end):
        if start > end:
            return [None]
        ans = []
        for nodeval in range(start, end + 1):
            left = self.dfs(start, nodeval - 1)
            right = self.dfs(nodeval + 1, end)
            for i in left:
                for j in right:
                    node = TreeNode(nodeval)
                    node.left, node.right = i, j
                    ans.append(node)
        return ans

def execute():
    n = 3
    sol = Solution()
    print(sol.generateTrees(n))


if __name__ == "__main__":
    execute()


