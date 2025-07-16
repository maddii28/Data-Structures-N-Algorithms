def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        intervals.append(newInterval)
        intervals.sort()
        results = [intervals[0]]
        
        for i in range(1,len(intervals)):
            if results[-1][0] <= intervals[i][0] <= results[-1][1]:
                if results[-1][1] >= intervals[i][1]:
                    continue
                else:
                    a = intervals[i][1]
                    results[-1][1] = a
                    continue
            else:
                results.append(intervals[i])
                
        return results

#better approach 
