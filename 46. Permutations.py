class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.ans = []
        self.dfs(nums, [])
        return self.ans
    
    def dfs(self, nums, path):
        if not nums:
            self.ans.append(path)
        for index, value in enumerate(nums):
            self.dfs(nums[:index] + nums[index + 1:], path + [value])


def execute() -> object:
    nums=[1,2,3]
    sol=Solution()
    print(sol.permute(nums))

if __name__=="__main__":
    execute()

# class Solution:
#     def permute(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[List[int]]
#         """
#         if len(nums) <= 1:
#             return [nums]
#         ans = []
#         for index, value in enumerate(nums):
#             for elems in self.permute(nums[:index] + nums[index + 1:]):
#                 ans.append([value] + elems)
#         return ans