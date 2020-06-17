# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        intervals = sorted(intervals, key=lambda x: x[0])
        ans = []
        for interval in intervals:
            if len(ans) == 0 or ans[-1][1] < interval[0]:
                ans.append(interval)
            else:
                ans[-1][1] = max(ans[-1][1], interval[1])
        return ans

def execute() -> object:
    intervals = [[1,3],[2,6],[8,10],[15,18]]
    sol = Solution()
    print(sol.merge(intervals))


if __name__ == "__main__":
    execute()
