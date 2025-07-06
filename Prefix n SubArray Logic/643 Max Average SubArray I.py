class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        l, r = 0,0
        sum = 0
        while r < k:
            sum += nums[r]
            r+=1
        count = sum / k

        while r < len(nums):
            sum -= nums[l] 
            sum += nums[r]
            l += 1
            r += 1
            count = max(count, sum / k)

        return count
