class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        ans, stack, node = [-float('Inf')], [], root
        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            ans.append(node.val)
            if ans[-1] <= ans[-2]:
                return False
            node = node.right
        return True
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
    root = TreeNode(9)
    root.insertLeft(3)
    root.insertRight(20)
    sol = Solution()
    print(sol.isValidBST(root))

if __name__ == "__main__":
    execute()
