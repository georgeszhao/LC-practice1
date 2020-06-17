class Solution(object):
    def smallestSubSeqSum(self, array, x):
        """
        # Initilize length of smallest
        # subarray as n+1
        """
        ans, n = [], len(array)
        array.sort()
        while x > 0 and array:
            if array[-1] > x:
                ans.append(array[-1])
                x -= array[-1]
                break
            else:
                x -= array[-1]
                ans.append(array[-1])
                array.pop()
        if x > 0:
            return [n + 1, []]
        return [len(ans), ans]

def execute() -> object:
    array = [5,6,2,3,8]
    x = 12
    sol = Solution()
    print(sol.smallestSubSeqSum(array, x))

if __name__ == "__main__":
    execute()