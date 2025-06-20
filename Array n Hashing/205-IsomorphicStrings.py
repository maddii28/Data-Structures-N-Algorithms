#205. Isomorphic Strings

#Given two strings s and t, determine if they are isomorphic.
#Two strings s and t are isomorphic if the characters in s can be replaced to get t.
#All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

#Example 1:
#Input: s = "egg", t = "add"
#Output: true

#Explanation:
#The strings s and t can be made identical by:
#Mapping 'e' to 'a'.
#Mapping 'g' to 'd'.

#Example 2:
#Input: s = "foo", t = "bar"
#Output: false

#Explanation:
#The strings s and t can not be made identical as 'o' needs to be mapped to both 'a' and 'r'.

#Example 3:
#Input: s = "paper", t = "title"
#Output: true



class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_map = {}
        t_map = {}
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            s_char = s[i]
            t_char = t[i]
            if s_char not in s_map:
                s_map[s_char] = []
            if t_char not in t_map:
                t_map[t_char] = []
            s_map[s_char].append(i)
            t_map[t_char].append(i)
        return list(s_map.values()) == list(t_map.values())