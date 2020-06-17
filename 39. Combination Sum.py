class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ans = []
        candidates.sort()
        self.dfs(candidates, target, 0, [], ans)
        return ans

    def dfs(self, candidates, target, start, path, ans):
        if target == 0:
            ans.append(path[:])
            return
        for i in range(start, len(candidates)):
            if candidates[i] <= target:
                path.append(candidates[i])
                self.dfs(candidates, target - candidates[i], i, path, ans)
                path.pop()

def execute() -> object:
    candidates = [2, 3, 6, 7, 8]
    target = 10
    sol = Solution()
    print(sol.combinationSum(candidates, target))


if __name__ == "__main__":
    execute()