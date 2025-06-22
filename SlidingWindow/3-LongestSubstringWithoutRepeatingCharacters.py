class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        map = set()
        max_length = 0 
        l, r = 0 , 0
        while r < len(s):
            while s[r] in map:
                    map.remove(s[l])
                    l += 1 
                    
            map.add(s[r])
            max_length = max(max_length,r-l+1) 
            r += 1 

        return max_length 