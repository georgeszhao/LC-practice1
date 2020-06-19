class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []

        self.dict = {'2': ['a', 'b', 'c'],
                     '3': ['d', 'e', 'f'],
                     '4': ['g', 'h', 'i'],
                     '5': ['j', 'k', 'l'],
                     '6': ['m', 'n', 'o'],
                     '7': ['p', 'q', 'r', 's'],
                     '8': ['t', 'u', 'v'],
                     '9': ['w', 'x', 'y', 'z']}
        self.ans = []
        self.dfs(digits, [], 0)
        return self.ans

    def dfs(self, digits, combination, index):
        if len(combination) == len(digits):
            self.ans.append("".join(x for x in combination))
            return
        for letter in self.dict[digits[index]]:
            combination.append(letter)
            self.dfs(digits, combination, index + 1)
            combination.pop()