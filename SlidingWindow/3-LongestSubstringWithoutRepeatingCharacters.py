#3. Longest Substring Without Repeating Characters

#Given a string s, find the length of the longest substring without duplicate characters.

#Example 1:
#Input: s = "abcabcbb"
#Output: 3
#Explanation: The answer is "abc", with the length of 3.

#Example 2:
#Input: s = "bbbbb"
#Output: 1
#Explanation: The answer is "b", with the length of 1.

#Example 3:
#Input: s = "pwwkew"
#Output: 3
#Explanation: The answer is "wke", with the length of 3.
#Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

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