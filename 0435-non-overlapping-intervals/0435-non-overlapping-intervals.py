class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        """

    [1,2],[1,3],[2,3],[3,4]

    result = [1,2], 
    i think i want to use a stack

    result is how i check and im going till the end of intervals

    result starts with 2 
    if curr interval 0 < prev interval in result increment then pop stack of result
    then check if next interval i is it then keep going until end of interval


        """

        if not intervals or len(intervals) == 1:
            return 0

        intervals.sort()
        result = [intervals[0]]
        count = 0

        for i in range(1, len(intervals)):
            if intervals[i][0] < result[-1][1]:
                count +=1

                if intervals[i][1] < result[-1][1]:
                    result[-1] = intervals[i]

            else:
                result.append(intervals[i])

        return count
            
