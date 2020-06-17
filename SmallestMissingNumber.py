class Solution(object):
    def SmallestMissingNumber(self, array):
        left, right = 0, len(array) - 1
        while left <= right:
            if array[left] != left:
                return left
            mid = left + (right - left) // 2
            if array[mid] == mid:
                left = mid + 1
            else:
                right = mid

def execute() -> object:
    array = [0, 1, 3, 4, 8, 9]
    sol = Solution()
    print(sol.SmallestMissingNumber(array))

if __name__ == "__main__":
    execute()