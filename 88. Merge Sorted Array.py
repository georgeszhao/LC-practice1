class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        p1, p2, end = m-1, n-1, m+n-1
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] < nums2[p2]:
                nums1[end] = nums2[p2]
                p2 -= 1
            else:
                nums1[end] = nums1[p1]
                p1 -= 1
            end -= 1
        if p1 <= 0:
            nums1[: p2+1] = nums2[: p2+1]
        return nums1

def execute() -> object:
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3
    sol = Solution()
    print(sol.merge(nums1, m, nums2, n))

if __name__ == "__main__":
    execute()
    
# # Javascript
# var merge = function(nums1, m, nums2, n) {
#     let i = m - 1;  
#     let j = n - 1;
#     let k = m + n - 1;
#     while(i >= 0 && j >= 0) {
#         if(nums2[j] >= nums1[i]) {
#             nums1[k] = nums2[j];
#             j--;
#             k--;
#         } else {
#             nums1[k] = nums1[i];
#             i--;
#             k--;
#         }
#     } 
#     // j < 0, nums1's looping is over, then continue nums2
#      while(j >= 0) {
#         nums1[k] = nums2[j];
#         j--;
#         k--;
#     }
# };
