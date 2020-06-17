class Solution(object):
    def nextGreaterElement(self, n):
        """
        :type n: int
        :rtype: int
        https://www.geeksforgeeks.org/least-greater-number-with-same-digit-sum/
        divide the number into 4 regions :
        1st: Trailing zeros .
        2nd: The lowest digit not in Region 1.
        3rd: Consecutive 9s starting with the digit above Region 2.
        4th: All remaining digits.
        """
        if 0 < n < 10:
            return 10 + (n - 1)
        nums = [0] + [int(x) for x in str(n)]
        # for storing 4 regions
        a1, a2, a3, a4 = [], [], [], []
        left, right = 0, len(nums) - 1  # first and last index
        # trailing zeros region1
        while nums[right] == 0:
            a1.append(0)
            right -= 1
        # lowest region(region 2) not in region 1
        a2.append(nums[right])
        right -= 1
        # Consecutive 9's (region 3)
        while nums[right] == 9:
            a3.append(9)
            right -= 1
        while left <= right:  # 4th region
            a4.append(nums[left])
            left += 1
        if a4:
            a4[-1] += 1  # Region4 + 1
        elif not a4 and a2[0] > 1:
            a4.append(a2[0] - 1)
        else:
            a4.append(1)
        a2[0] -= 1  # Region2 -1
        # Calculating the result
        i, j = len(a3) - 1, len(nums) - 1
        # Copying the third region
        while i >= 0:
            nums[j] = a3[i]
            j -= 1
            i -= 1
        # Copying the 2nd region
        i = len(a2) - 1
        while i >= 0:
            nums[j] = a2[i]
            j -= 1
            i -= 1
        # Copying the 1st region
        i = len(a1) - 1
        while i >= 0:
            nums[j] = a1[i]
            j -= 1
            i -= 1
        # Copying the 4th region
        i = len(a4) - 1
        while i >= 0:
            nums[j] = a4[i]
            j -= 1
            i -= 1
        s = [str(i) for i in nums]
        return int(''.join(s))

def execute() -> object:
    n = 2000
    sol = Solution()
    print(sol.nextGreaterElement(n))


if __name__ == "__main__":
    execute()

# class Solution:
#     """
#     @param A: An array of integers
#     @return: An integer
#     """
#     def question5(self, nums1, nums2):
#         m, n, sum1, sum2 = len(nums1), len(nums2), sum(nums1), sum(nums2)
#         if max(m, n) * 1 > min(m, n) * 6:
#             return -1
#         return min(self.helper(nums1, sum2), self.helper(nums2, sum1))
#
#     def helper(self, nums, target):
#         ans, nums_sum = 0, sum(nums)
#         nums.sort()
#         diff = nums_sum - target
#         if diff < 0:
#             for num in nums:
#                 if num - diff <= 6:
#                     num -= diff
#                     return ans + 1
#                 else:
#                     diff += (6 - num)
#                     num = 6
#                     ans += 1
#         if diff > 0:
#             for num in nums[::-1]:
#                 if num - diff >= 1:
#                     num -= diff
#                     return ans + 1
#                 else:
#                     diff -= (num - 1)
#                     num = 1
#                     ans += 1
#         return ans if diff == 0 else float('inf')
#
# def execute() -> object:
#     # nums1, nums2 = [2, 3, 1, 1, 2], [5, 4, 6]
#     nums1, nums2 = [5, 4, 1, 2, 6, 5], [2]
#     sol = Solution()
#     print(sol.question5(nums1, nums2))
#
# if __name__=="__main__":
#     execute()