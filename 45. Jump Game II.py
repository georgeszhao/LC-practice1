class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans, end, max_pos = 0, 0, 0
        for index, value in enumerate(nums[:-1]):
            max_pos = max(max_pos, index + value)
            if index == end:
                end = max_pos
                ans += 1
        return ans

def execute():
    nums = [2, 3, 1, 1, 4]
    sol = Solution()
    print(sol.jump(nums))

if __name__ == "__main__":
    execute()

# class Solution(object):
#     def jump(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         dp, i = [0], 0
#         while i < len(nums) - 1 and len(dp) < len(nums):
#             while i + nums[i] >= len(dp):
#                 dp.append(dp[i] + 1)
#             i += 1
#         return dp[-1]