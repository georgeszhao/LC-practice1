class Solution(object):
    def subsets(self, my_set):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums = list(my_set)
        self.ans = []
        self.dfs(sorted(nums), [], 0)
        return sorted(set(tuple(x) for x in self.ans))

    def dfs(self, nums, path, index):
        self.ans.append(path)
        for i in range(index, len(nums)):
            self.dfs(nums, path + [nums[i]], i + 1)


def execute():
    my_set = {1, 2, 3}
    sol = Solution()
    print(sol.subsets(my_set))


if __name__ == "__main__":
    execute()


