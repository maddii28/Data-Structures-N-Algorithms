class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]: 
        intervals.sort() #O(nlogn) 
        i = 0
        results = []
        while i < len(intervals)-1:
            if intervals[i][0] <= intervals[i+1][0] <= intervals[i][1]:
                    if intervals[i][1] > intervals[i+1][1]:
                        intervals.pop(i+1)
                    else:
                        a = intervals[i+1][1]
                        intervals[i][1] = a 
                        intervals.pop(i+1) #.pop() leads to shifting all the elements which could lead to O(n^2)
            else:
                i+=1
        return intervals
    
#TimeComplexity - O(nlogn + n^2)
    
#first time approach - not time optimum 
#Note : - if you are iterating through a list , 
# its better to use another results list insteads of mutatuing original one 

#Better Approach:
class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]: 
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