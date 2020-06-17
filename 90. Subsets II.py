class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.ans = []
        self.dfs(sorted(nums), [])
        return self.ans

    def dfs(self, nums, path):
        self.ans.append(path[::])
        for index, value in enumerate(nums):
            if index and nums[index] == nums[index - 1]:
                continue
            path.append(value)
            self.dfs(nums[index + 1:], path)
            path.pop()

def execute() -> object:
    nums = [1, 2, 2]
    sol = Solution()
    print(sol.subsetsWithDup(nums))

if __name__ == "__main__":
    execute()