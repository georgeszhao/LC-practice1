class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        ans, left, right = 0, 0, len(height) - 1
        while left < right:
            h = min(height[left], height[right])
            ans = max(ans, h * (right - left))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return ans

def execute() -> object:
    height = [0,1,0,2,1,0,1,3,2,1,2,1]
    sol = Solution()
    print(sol.maxArea(height))

if __name__ == "__main__":
    execute()

