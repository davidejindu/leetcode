"""
your given an array of intergers

some of the elements overlap
return the array with merging intervals so non overlap

[1,3],[1,6],[8,10],[15,18]
                     ^
                          

result = [[1,6]]

"""
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        result = []
        intervals.sort()

        for i in range(1, len(intervals)):
            if intervals[i][0] > intervals[i-1][1]:
                result.append(intervals[i-1])
            else:
                intervals[i] = [
                    min(intervals[i-1][0], intervals[i][0]),
                    max(intervals[i-1][1], intervals[i][1])
                    ]

        result.append(intervals[len(intervals) - 1])

        return result
    
        