"""
intervals array is non overlapping
intervals are in sorted order by the first index of each element 

im given a new element that has the start and end of another interval

im suppose to insert the new interval into the intervals array so it remains sorted

input: intervals = [[1,2],[3,8],[6,7],[8,10],[12,16]], newInterval = [3,8]
                                  ^


output: [[1,5], [6,9]]

result = [[1,2]]

if first index in newInterval is less than first index in interval
we can just append new interval to beginning of array and keep everything same
elif first index is greater than end[i] then we append intervali to a new array and continue
the check 
else
then we know its between so its a merge
then we make intervals[i] = [min(start,start) max(end,end)] and set newInterval to interval[i]
now if first index is greater than the last one 

we will have an empty result so since we can just return whenever the newInterval i is less than the start of starti if we dont return that means at the end of loop we have to append newInteval to end of result then return since we kept on continuing


"""
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []

        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]:
                result.append(newInterval)
                return result + intervals[i:]
            elif newInterval[0] > intervals[i][1]:
                result.append(intervals[i])
            else:
                intervals[i] = [
                    min(intervals[i][0], newInterval[0]),
                    max(intervals[i][1], newInterval[1])
                ]
                newInterval = intervals[i]

        result.append(newInterval)
        return result
        