class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return []
        up, down = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1
        ans, direction = [], 0
        while up <= down and left <= right:
            if direction == 0:
                for j in range(left, right + 1):
                    ans.append(matrix[up][j])
                up += 1
            if direction == 1:
                for i in range(up, down + 1):
                    ans.append(matrix[i][right])
                right -= 1
            if direction == 2:
                for j in range(right, left - 1, -1):
                    ans.append(matrix[down][j])
                down -= 1
            if direction == 3:
                for i in range(down, up - 1, -1):
                    ans.append(matrix[i][left])
                left += 1
            direction = (direction + 1) % 4
        return ans

def execute() -> object:
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    sol = Solution()
    print(sol.spiralOrder(matrix))

if __name__ == "__main__":
    execute()

#  /** Javascript
#  * @param {number[][]} matrix
#  * @return {number[]}
#  */
# var spiralOrder = function(matrix) {
#     if(matrix === null || matrix.length === 0) return [];
    
#     let ans = [];
#     let direction = 0;
#     let up = 0;
#     let down = matrix.length - 1;
#     let left = 0;
#     let right = matrix[0].length - 1;
    
#     while(up <= down && left <= right) {
#         if (direction == 0) {
#             for (let j = left; j <= right; j++) {
#                 ans.push(matrix[up][j]);
#             }
#         up++;
#         }
        
#         if (direction == 1) {
#             for (let i = up; i <= down; i++) {
#                 ans.push(matrix[i][right]);
#             }
#         right--;
#         }
        
#         if (direction == 2) {
#             for (let j = right; j >= left; j--) {
#                 ans.push(matrix[down][j]);
#             }
#         down--;
#         }
        
#         if (direction == 3) {
#             for (let i = down; i >= up; i--) {
#                 ans.push(matrix[i][left]);
#             }
#         left++;
#         }
#         direction = (direction + 1) % 4;
#     }
#     return ans;
# };

