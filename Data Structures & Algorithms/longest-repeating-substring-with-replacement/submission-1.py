class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        freq = {}
        max_freq = 0
        result = 0
        
        
        for right in range(0, len(s)):

            freq[s[right]] = freq.get(s[right], 0) + 1
            max_freq = max(max_freq, freq[s[right]])

            window_size = right - left + 1
            while left < right and window_size - max_freq > k:
                freq[s[left]] -= 1
                left += 1
                window_size = right - left + 1
            
            result = max(result, right - left + 1)
                
        return result
            

            
