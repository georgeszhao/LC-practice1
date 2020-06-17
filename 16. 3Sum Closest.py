import sys
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        ans, n = sys.maxsize, len(nums)
        if not nums or n < 3:
            return []
        if n == 3:
            return sum(nums)
        nums.sort()
        for i in range(n - 2):
            left, right = i + 1, n - 1
            while left < right:
                cur_sum = nums[i] + nums[left] + nums[right]
                if abs(cur_sum - target) < abs(ans - target):
                    ans = cur_sum
                if cur_sum == target:
                    return target
                elif cur_sum < target:
                    left += 1
                else:
                    right -= 1
        return ans

def execute() -> object:
    nums, target = [-1,2,1,-4], 1
    sol = Solution()
    print(sol.threeSumClosest(nums, target))

if __name__ == "__main__":
    execute()