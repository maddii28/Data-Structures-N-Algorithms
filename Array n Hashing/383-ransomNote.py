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
