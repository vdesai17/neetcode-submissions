class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        s_count = {}
        t_count = {}

        #if s and t have different lenghts trivially cannot be an anagram
        if len(s) != len(t):
            return False 
        
        for char in range(0, len(s)):
            s_count[s[char]] = s_count.get(s[char], 0) + 1
            t_count[t[char]] = t_count.get(t[char], 0) + 1
        
        return s_count == t_count 
 


