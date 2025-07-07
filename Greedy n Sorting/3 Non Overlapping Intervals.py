class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        intervals.sort(key = lambda x: x[1])
        end = float('-inf')
        count = 0 

        for i in intervals:
            if i[0] >= end:
                end = i[1]
                count += 1
        
        return len(intervals) - count 