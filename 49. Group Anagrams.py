class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dict = {}
        for value in strs:
            key = ''.join(sorted(value))
            dict[key] = dict.get(key, []) + [value]
        return dict.values()

def execute():
    strs = ["eat","tea","tan","ate","nat","bat"]
    sol = Solution()
    print(sol.groupAnagrams(strs))

if __name__ == "__main__":
    execute()


