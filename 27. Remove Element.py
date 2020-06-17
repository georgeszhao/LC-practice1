class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        j = len(nums) - 1
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] == val:
                nums[i], nums[j] = nums[j], nums[i]
                j -= 1
        return j + 1


def execute() -> object:
    nums= [3, 2, 2, 3]
    val= 3
    sol = Solution()
    print(sol.removeElement(nums, val))


if __name__ == "__main__":
    execute()
