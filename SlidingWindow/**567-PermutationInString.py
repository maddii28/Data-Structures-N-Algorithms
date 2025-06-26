#567. Permutation in String

#Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.
#In other words, return true if one of s1's permutations is the substring of s2.

#Example 1:
#Input: s1 = "ab", s2 = "eidbaooo"
#Output: true
#Explanation: s2 contains one permutation of s1 ("ba").

#Example 2:
#Input: s1 = "ab", s2 = "eidboaoo"
#Output: false

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1_map = {}
        for c in s1:
            s1_map[c] = s1_map.get(c, 0) + 1

        s2_map = {}
        for i in range(len(s1)):
            s2_map[s2[i]] = s2_map.get(s2[i], 0) + 1

        l = 0
        for r in range(len(s1), len(s2)):
            if s1_map == s2_map:
                return True
            s2_map[s2[l]] -= 1
            if s2_map[s2[l]] == 0:
                del s2_map[s2[l]]
            l += 1
            s2_map[s2[r]] = s2_map.get(s2[r], 0) + 1

        return s1_map == s2_map