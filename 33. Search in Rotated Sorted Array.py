class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left, right = 0, len(nums)
        while left < right:
            mid = left + (right - left) // 2
            if target < nums[0] < nums[mid]:
                left = mid + 1
            elif target >= nums[0] > nums[mid]:
                right = mid
            elif target > nums[mid]:
                left = mid + 1
            elif target < nums[mid]:
                right = mid
            else:
                return mid
        return -1

def execute() -> object:
    nums = [4,5,6,7,0,1,2]
    target = 0
    sol = Solution()
    print(sol.search(nums, target))

if __name__ == "__main__":
    execute()

# class Solution(object):
#     def search(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: int
#         """
#         if not nums or len(nums) == 0:
#             return -1
#         left, right = 0, len(nums) - 1
#         while left <= right:
#             mid = left + (right - left) // 2
#             if nums[mid] == target:
#                 return mid
#             if nums[left] < nums[mid]:
#                 if nums[left] <= target < nums[mid]:
#                     right = mid - 1
#                 else:
#                     left = mid + 1
#             elif nums[left] > nums[mid]:
#                 if nums[mid] < target <= nums[right]:
#                     left = mid + 1
#                 else:
#                     right = mid - 1
#             else:
#                 left += 1
#         return -1


# class Solution(object):
#     def search(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: int
#         """
#         left, right = 0, len(nums)
#         while left < right:
#             mid = left + (right - left) // 2
#             if target < nums[0] < nums[mid]:
#                 left = mid + 1
#             elif target >= nums[0] > nums[mid]:
#                 right = mid
#             elif target > nums[mid]:
#                 left = mid + 1
#             elif target < nums[mid]:
#                 right = mid
#             else:
#                 return mid
#         return -1