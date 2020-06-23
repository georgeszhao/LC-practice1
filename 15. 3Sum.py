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
            if nums[i] + nums[i + 1] + nums[i + 2] > 0:
                break
            if (i and nums[i] == nums[i - 1]) or (nums[i] + nums[n - 2] + nums[n - 1] < 0):
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

# /** Javascript
#  * @param {number[]} nums
#  * @return {number[][]}
#  */
# var threeSum = function(nums) {
#     nums = nums.sort((a, b) => a - b);
#     let n = nums.length;
#     if (n < 3 || nums[0] > 0 || nums[n - 1] < 0)
#             return [];
#     let ans = [];
    
#     for(let i = 0; i < n - 2; i++) {
#         if (nums[i] + nums[i + 1] + nums[i + 2] > 0) break;
        
#         if (i > 0 && nums[i] === nums[i - 1]) continue;
        
#         if (nums[i] + nums[n - 2] + nums[n - 1] < 0) continue;
        
#         let left = i + 1,
#             right = n - 1;
#         while(left < right) {
#             let target = nums[i] + nums[left] + nums[right];
#             if(target === 0) {
#                 ans.push([nums[i], nums[left], nums[right]]);
#                 left ++;
#                 right --;
#                 while(left < right && nums[left] === nums[left - 1]) {
#                     left ++;
#                 }
#                 while(left < right && nums[right] === nums[right + 1]) {
#                     right --;
#                 }
#             }
#             else if(target < 0) {
#                 left ++;
#             }
#             else {
#                 right --;
#             }
#         }
#     }
    
#     return ans;
# };

