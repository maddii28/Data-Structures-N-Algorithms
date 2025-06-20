#242. Valid Anagram
#Easy

#Topics
#premium lock icon
#Companies
#Given two strings s and t, return true if t is an anagram of s, and false otherwise.

 

#Example 1:

#Input: s = "anagram", t = "nagaram"

#Output: true

#Example 2:

#Input: s = "rat", t = "car"

#Output: false


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_map = {}
        t_map = {}
        for i in range(len(s)):
            if s[i] not in s_map:
                s_map[s[i]] = 0 
            if t[i] not in t_map:
                t_map[t[i]] = 0
            s_map[s[i]] += 1
            t_map[t[i]] += 1
        
        return s_map == t_map