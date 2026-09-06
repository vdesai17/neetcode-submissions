class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        window = set()
        maxLen = 0
        left = 0
        for char in s:

            while char in window:
                # shrink window from left
                window.remove(s[left])
                left += 1

            window.add(char)
            maxLen = max(maxLen, len(window))
        
        
        return maxLen

        