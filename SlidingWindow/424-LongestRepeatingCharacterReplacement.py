#424. Longest Repeating Character Replacement

#You are given a string s and an integer k. 
#You can choose any character of the string and change it to any other uppercase English character. 
#You can perform this operation at most k times.
#Return the length of the longest substring containing the same letter 
#you can get after performing the above operations.

#Example 1:
#Input: s = "ABAB", k = 2
#Output: 4
#Explanation: Replace the two 'A's with two 'B's or vice versa.

#Example 2:
#Input: s = "AABABBA", k = 1
#Output: 4
#Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
#The substring "BBBB" has the longest repeating letters, which is 4.
#There may exists other ways to achieve this answer too.


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0,0
        map = {}
        res = 0 
        mat = 0
        while r < len(s):
            if s[r] not in map:
                map[s[r]] = 0 
            map[s[r]]+=1
            mat = max(mat,map[s[r]])
            if (r-l+1) - mat > k:
                map[s[l]] -= 1
                l+=1
            res = max(res, r-l+1)
            r +=1 

        return res