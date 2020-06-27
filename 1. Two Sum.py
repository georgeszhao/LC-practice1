class Solution:
    def twoSum(self, nums, target):
        n = len(nums)
        A = sorted(zip(nums, range(n)))
        left, right = 0, n-1
        while left < right:
            if A[left][0] + A[right][0] == target:
                return [A[left][1], A[right][1]] if A[left][1]< A[right][1] else [A[right][1], A[left][1]]
            elif A[left][0] + A[right][0] < target:
                left += 1
            else: 
                right -= 1

    nums=[7, 2,10,11]
    target=9
    print(twoSum(nums, target))


# class Solution(object):
#     def twoSum(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: List[int]
#         """
#         dict = {}
#         for index, value in enumerate(nums):
#             if value in dict:
#                 return [dict[value], index]
#             dict[target - value] = index

# R solution to Leetcode.
# twoSum = function(nums, target){
#   n = length(nums)
#   a = cbind(nums, 1:n)
#   A = as.matrix(a[order(a[,1]), ])
#   left = 1
#   right = n
#   while (left < right){
#     if (A[left, 1] + A[right, 1] == target){
#         ans = c(A[left, 2], A[right, 2])  
#         break
#     }
#     else if (A[left, 1] + A[right, 1] < target){
#       left =  left + 1
#     }
#     else {
#       right = right - 1
#     }
#   }
#    sort(ans)
# }

# twoSum(c(7, 2, 10, 11), 9)  

# /** Javascript
#  * @param {number[]} nums
#  * @param {number} target
#  * @return {number[]}
#  */
# var twoSum = function(nums, target) {
#     const map = {};
#     for(let i = 0; i < nums.length; i++) {
#         if(map[nums[i]] !== undefined) {
#             return [map[nums[i]], i];
#         }
#         else {
#             map[target - nums[i]] = i;
#         }
#     }
# };
