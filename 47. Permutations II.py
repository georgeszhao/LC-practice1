class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.ans = []
        self.dfs(sorted(nums), [])
        return self.ans

    def dfs(self, nums, path):
        if not nums:
            self.ans.append(path)
            return
        for index, value in enumerate(nums):
            if index and nums[index] == nums[index - 1]:
                continue
            self.dfs(nums[:index] + nums[index + 1:], path + [value])

def execute() -> object:
    nums = [1, 2, 2]
    sol = Solution()
    print(sol.permuteUnique(nums))

if __name__ == "__main__":
    execute()