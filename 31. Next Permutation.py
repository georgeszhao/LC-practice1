class Solution:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        for i in range(n - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                for j in range(n - 1, i, -1):
                    if nums[i] < nums[j]:
                        break
                nums[i], nums[j] = nums[j], nums[i]
                nums[i + 1:] = reversed(nums[i + 1:])
                return nums
        nums.reverse()
        return nums

def execute() -> object:
    nums = [3, 2, 1]
    sol = Solution()
    print(sol.nextPermutation(nums))

if __name__=="__main__":
    execute()

# class Solution:
#     def nextPermutation(self, nums: List[int]) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         i = len(nums) - 2
#         while i >= 0 and nums[i] >= nums[i + 1]:
#             i -= 1
#         if i >= 0:
#             j = len(nums) - 1
#             while j > i and nums[i] >= nums[j]:
#                 j -= 1
#             nums[i], nums[j] = nums[j], nums[i]
#         nums[i + 1:] = reversed(nums[i + 1:])
#         return nums