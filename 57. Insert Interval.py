
class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        ans=[]
        insertPos=0

        for i in intervals:
            if i.end< newInterval.start:
                ans.append(i)
                insertPos+=1

            elif i.start> newInterval.end:
                ans.append(i)

            else:
                newInterval.start=min(i.start, newInterval.start)
                newInterval.end=max(i.end, newInterval.end)

        ans.insert(insertPos, newInterval)
        return ans

def execute() -> object:
    intervals = [[1,3],[6,9]]
    newInterval= [2, 5]
    sol = Solution()
    print(sol.insert(intervals, newInterval))


if __name__ == "__main__":
    execute()
