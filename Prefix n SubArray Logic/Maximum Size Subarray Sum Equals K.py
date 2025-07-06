#Given an array nums and a target value k, find the maximum length of a subarray
#that sums to k. If there isn't one, return 0 instead.

#Note:
#he sum of the entire nums array is guaranteed to fit within the 32-bit signed integer range.

#Example 1:

#Input: nums = [1, -1, 5, -2, 3], k = 3
#Output: 4
#Explanation: The subarray [1, -1, 5, -2] sums to 3 and is the longest.
#xample 2:

#Input: nums = [-2, -1, 2, 1], k = 1
#Output: 2
#Explanation: The subarray [-1, 2] sums to 1 and is the longest.
#Follow Up:
#Can you do it in O(n) time?


def maxSubArrayLen(nums, k):
        sum = 0 
        count = 0
        hass = {}
        hass[0] = -1
        
        for i in range(len(nums)):

            sum += nums[i]

            if (sum-k) in hass:
                count = max(count,i+-hass[sum-k])

            if sum not in hass:
                hass[sum] = i
        
        return count

print(maxSubArrayLen([1, -1, 5, -2, 3], 3))  # Output: 4 ([1, -1, 5, -2])
print(maxSubArrayLen([-2, -1, 2, 1], 1))     # Output: 2 ([-1, 2])
print(maxSubArrayLen([1, 2, 3], 3))          # Output: 2 ([1, 2])
print(maxSubArrayLen([1, 2, 3], 6))          # Output: 3 ([1, 2, 3])