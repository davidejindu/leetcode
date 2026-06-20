"""
find minimum overlapping intervals that can be removed so no intervals overlap

so the goal is first sort it 


[1,2], [1,3], [2,3],[3,4]

start at 1 and if it overlaps with element behind it whatever interval has larger end
remove it then increment

"""

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key= lambda x: x[0])
        count = 0

        for i in range(1, len(intervals)):
            if intervals[i][0] < intervals[i - 1][1]:
                count += 1
                if intervals[i-1][1] < intervals[i][1]:
                    intervals[i] = intervals[i - 1]

        return count 

        return count