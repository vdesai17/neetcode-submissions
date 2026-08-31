class Solution:
    def minWindow(self, s: str, t: str) -> str:

        left, right = 0, 0
        freq_t = dict()
        window = dict()
        have = 0
        res = [-1,-1]
        res_len = float("inf")

        # create freq map for chars in t
        for char in t:
            if char not in freq_t:
                freq_t[char] = 1
            else:
                freq_t[char] += 1
        
        # ex) {x: 1, y: 1, z: 1}
        need = len(freq_t)

        for right in range(len(s)):
            window[s[right]] = 1 + window.get(s[right],0)

            if s[right] in freq_t and window[s[right]] == freq_t[s[right]]:
                have += 1

            while have == need:
                if (right-left) + 1 < res_len:
                    res = [left, right]
                    res_len = right - left + 1
                window[s[left]] -= 1
                if s[left] in freq_t and window[s[left]] < freq_t[s[left]]:
                    have -= 1
                left += 1
        
        l, r = res
        return s[l : r + 1] if res_len != float("inf") else ""

            

            







        


        