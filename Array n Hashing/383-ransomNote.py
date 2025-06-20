#383. Ransom Note

#Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.
#Each letter in magazine can only be used once in ransomNote.

#Example 1:
#Input: ransomNote = "a", magazine = "b"
#Output: false

#Example 2:
#Input: ransomNote = "aa", magazine = "ab"
#Output: false

#Example 3:
#Input: ransomNote = "aa", magazine = "aab"
#Output: true

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mag_map = {}
        for i in range(len(magazine)):
            if magazine[i] not in mag_map:
                mag_map[magazine[i]] = 0
            mag_map[magazine[i]] += 1

        for i in range(len(ransomNote)):
            if ransomNote[i] in mag_map:
                mag_map[ransomNote[i]] -= 1 
                if mag_map[ransomNote[i]] < 0:
                    return False
            else:
                return False
        return True
