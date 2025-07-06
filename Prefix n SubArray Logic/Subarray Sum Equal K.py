class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        sum = 0 
        res = 0
        has = {}
        has[0] = 1

        for i in nums:
            sum += i 
            if (sum - k) in has:
                res += has[sum-k]
            if sum not in has:
                has[sum] = 0
            has[sum] += 1
        return res