class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n, start = len(nums), 0
        if n <= 1:
            return n
        for i in range(1, n):
            if nums[i] != nums[start]:
                start += 1
                nums[i], nums[start] = nums[start], nums[i]
        return start + 1

def execute() -> object:
    nums = [1,1,2]
    sol = Solution()
    print(sol.removeDuplicates(nums))

if __name__=="__main__":
    execute()
