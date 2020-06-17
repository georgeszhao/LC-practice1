class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans, n = [], len(nums)
        nums.sort()
        if not nums or n < 3 or nums[0] > 0 or nums[-1] < 0:
            return []
        for i in range(n - 2):
            if i and nums[i] == nums[i - 1]:
                continue
            left, right = i + 1, n - 1
            while left < right:
                cur_sum = nums[i] + nums[left] + nums[right]
                if cur_sum == 0:
                    ans.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif cur_sum > 0:
                    right -= 1
                else:
                    left += 1
        return ans

def execute():
    nums = [-1, 0, 1, 2, -1, -4]
    sol = Solution()
    print(sol.threeSum(nums))

if __name__ == "__main__":
    execute()


