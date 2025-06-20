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