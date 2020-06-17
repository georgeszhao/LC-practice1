class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ans, n = [], len(nums)
        if not nums or n < 4:
            return []
        nums.sort()
        for i in range(n - 3):
            if i and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, n - 2):
                if j != i + 1 and nums[j] == nums[j - 1]:
                    continue
                left, right = j + 1, n - 1
                while left < right:
                    cur_sum = nums[i] + nums[j] + nums[left] + nums[right]
                    if cur_sum == target:
                        ans.append([nums[i], nums[j], nums[left], nums[right]])
                        left += 1
                        right -= 1
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1
                    elif cur_sum > target:
                        right -= 1
                    else:
                        left += 1
        return ans

def execute():
    nums, target = [-1, 0, 1, 2, -1, -4], 1
    sol = Solution()
    print(sol.fourSum(nums, target))

if __name__ == "__main__":
    execute()


