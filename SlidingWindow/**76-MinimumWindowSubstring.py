#76. Minimum Window Substring

#Given two strings s and t of lengths m and n respectively, return the 
#minimum window substring of s such that every character in t (including duplicates) 
#is included in the window. 
#If there is no such substring, return the empty string "".

#The testcases will be generated such that the answer is unique.

#Example 1:
#Input: s = "ADOBECODEBANC", t = "ABC"
#Output: "BANC"
#Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.

#Example 2:
#Input: s = "a", t = "a"
#Output: "a"
#Explanation: The entire string s is the minimum window.

#Example 3:
#Input: s = "a", t = "aa"
#Output: ""
#Explanation: Both 'a's from t must be included in the window.
#Since the largest window of s only has one 'a', return empty string.

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l, r = 0, 0
        map = {}
        t_map = {}

        for i in range(len(t)):
            if t[i] not in t_map:
                t_map[t[i]] = 0
            t_map[t[i]] += 1

        min_len = float('inf')
        min_start = 0
        have = 0
        need = len(t_map)

        while r < len(s):
            if s[r] not in map:
                map[s[r]] = 0
            map[s[r]] += 1

            if s[r] in t_map and map[s[r]] == t_map[s[r]]:
                have += 1

            while have == need:
                if (r - l + 1) < min_len:
                    min_len = r - l + 1
                    min_start = l
                map[s[l]] -= 1
                if s[l] in t_map and map[s[l]] < t_map[s[l]]:
                    have -= 1
                l += 1

            r += 1

        return "" if min_len == float('inf') else s[min_start:min_start + min_len]