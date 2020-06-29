class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans, start, dict = 0, 0, {}
        for index, value in enumerate(s):
            if value in dict and dict[value] >= start:
                start = dict[value] + 1
            else:
                ans = max(ans, index - start + 1)
            dict[value] = index
        return ans

def execute() -> object:
    s = "abcabcbb"
    sol = Solution()
    print(sol.lengthOfLongestSubstring(s))

if __name__ == "__main__":
    execute()

# /** Javascript
#  * @param {string} s
#  * @return {number}
#  */
# var lengthOfLongestSubstring = function(s) {
#     if (s === '' || s.length === 0) return 0;
    
    
#     let start = 0;
#     let map = {};
#     let ans = 0;
    
#     for (let i = 0; i < s.length; i++) {
#         let ch = s[i];
#         // check if the char in the map, update the index position 
#         if (ch in map && map[ch] >= start) {
#             start = map[ch] + 1;
#         }
#         else {
#             ans = Math.max(ans, i - start + 1);
#         }
#         map[ch] = i;
#     }
#     return ans;
# };
