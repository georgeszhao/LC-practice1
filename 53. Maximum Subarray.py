class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [nums[0]] * len(nums)
        for i in range(1, len(nums)):
            dp[i] = dp[i - 1] + nums[i] if dp[i - 1] > 0 else nums[i]
        return max(dp)

def execute():
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    sol = Solution()
    print(sol.maxSubArray(nums))

if __name__ == "__main__":
    execute()