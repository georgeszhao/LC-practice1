class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums or target <= nums[0]:
            return 0
        if target > nums[-1]:
            return len(nums)
        for index, value in enumerate(nums):
            if target <= value:
                return index

def execute() -> object:
    nums = [1,3,5,6]
    target = 5
    sol = Solution()
    print(sol.searchInsert(nums, target))


if __name__ == "__main__":
    execute()

