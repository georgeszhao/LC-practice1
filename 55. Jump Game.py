class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        arrive = 0
        for index, value in enumerate(nums[:-1]):
            arrive = max(arrive, index + value)
            if arrive >= len(nums) - 1:
                return True
            if arrive <= index:
                return False
        return True

def execute():
    A = [2, 3, 1, 1, 4]
    sol = Solution()
    print(sol.canJump(A))

if __name__ == "__main__":
    execute()

# class Solution:
#     def canJump(self, A):
#         """
#         :type nums: List[int]
#         :rtype: bool
#         """
#         last_pos = len(A) - 1
#         for i in range(len(A) - 2, -1, -1):
#             if i + A[i] >= last_pos:
#                 last_pos = i
#         return last_pos == 0