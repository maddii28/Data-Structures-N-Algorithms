class Solution:
    def numSubarraysWithSum(self, nums: list[int], goal: int) -> int:
        count = 0 
        sum = 0 
        has = {}
        has[0] = 1
        
        for i in range(len(nums)):
            
            sum += nums[i]
            
            if (sum-goal) in has:
                count += has[sum-goal]
            
            if sum not in has:
                has[sum] = 0 
            
            has[sum] += 1 
        
        return count 