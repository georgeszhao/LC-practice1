class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        ans, stack, node = [], [], root
        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            ans.append(node.val)
            node = node.right
        return ans
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def insertLeft(self, newNode):
        if self.left is None:
            self.left = TreeNode(newNode)

    def insertRight(self, newNode):
        if self.right is None:
            self.right = TreeNode(newNode)

def execute() -> object:
    root = TreeNode(3)
    root.insertLeft(9)
    root.insertRight(20)
    sol = Solution()
    print(sol.inorderTraversal(root))

if __name__ == "__main__":
    execute()
