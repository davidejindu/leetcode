"""
return minimum # of intervals i need to remove to make the intervals non overlapping

intervals which touch are non overlapping

definetely have to sort first before anything 

[1,2],[1,3],[2,3],[3,4]
        ^

count = 1
yo so basically if you find an overlap increment count to 1 but then you want to 
make sure whatever end is smaller becomes i since its less likely to overlap
  


"""
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        count = 0
        intervals.sort()

        for i in range(1, len(intervals)):
            if intervals[i][0] < intervals[i-1][1]:
                count +=1
                intervals[i] = [
                    min(intervals[i][0],intervals[i-1][0]),
                    min(intervals[i][1],intervals[i-1][1])
                ]
                

        return count
        