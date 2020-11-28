class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        pars = [None]
        dict = {')': '(',
                '}': '{',
                ']': '['}
        for c in s:
            if c in dict and dict[c] == pars[-1]:
                pars.pop()
            else:
                pars.append(c)
        return len(pars) == 1

def execute() -> object:
    s= "()"
    sol = Solution()
    print(sol.isValid(s))


if __name__ == "__main__":
    execute()

    
# ### Javascript solution.
# var isValid = function(s) {
#     if(s === '' || s.length === 0) return true;
#     let dict = new Map([
#         ['(', ')'],
#         ['[', ']'],
#         ['{', '}'],
#         ['$', '$']
#     ]); 
#     let stack = [];
#     stack.push('$')
#     for (let c of s) {
#       if (dict.get(c) != null) {
#           stack.push(c);
#       } else if (dict.get(stack.pop()) != c) {
#               return false;
#       }
#     }
#     return stack.length == 1;
# }
