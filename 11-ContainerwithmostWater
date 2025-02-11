class Solution:
    def maxArea(self, height):
        l = 0
        r =len(height) - 1
        sum = 0
        while l < r:
            if sum < (r - l) * min (height[r], height[l]):
                sum = (r - l) * min (height[r] , height[l])
            if height[l] < height[r]:
                l = l + 1
            elif height[r] < height[l]:
                r = r - 1
            elif height[r] == height[l]:
                r = r - 1
        return sum
    