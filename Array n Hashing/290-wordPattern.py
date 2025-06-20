class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(pattern) != len(words):
            return False
        pattern_map = {}
        for i in range(len(pattern)):

            if pattern[i] not in pattern_map:
                pattern_map[pattern[i]] = words[i]
            
            if pattern_map[pattern[i]] != '' and pattern_map[pattern[i]] != words[i]:
                return False  
            
        if len(set(pattern_map.values())) != len(pattern_map.values()):
            return False
         
        return True 
