class Solution:
    """
    @param A: An array of integers
    @return: An integer
    """
    def firstMissingPositive(self, A):
        # write your code here
        n = len(A)
        if not A or not n:
            return 1
        for i in range(n):
            while 0 < A[i] <= n and A[A[i]-1] != A[i]:
                A[A[i] - 1], A[i] = A[i], A[A[i]-1]
        for j in range(n):
            if A[j] != j + 1:
                return j + 1
        return n + 1

def execute() -> object:
    A = [1, 3, 2]
    sol = Solution()
    print(sol.firstMissingPositive(A))

if __name__=="__main__":
    execute()
