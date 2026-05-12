class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        left = 0 
        myset = set()
        count = 0

        for right in range(len(s)):
            while s[right] in myset:
                myset.remove(s[left])
                left += 1
            myset.add(s[right])
            count = max(count, right - left + 1)
        return count


        # count = 0
        # myset = set()
        # countset = set()
        # j = 0

        # for i in range(0, len(s)):
        #     if s[i] not in myset:
        #         count += 1
        #         myset.add(s[i])
        #     else:
        #         j = i
        #         countset.add(count)
        #         count = 0 
        #         myset = set()


        # return max(countset)
        