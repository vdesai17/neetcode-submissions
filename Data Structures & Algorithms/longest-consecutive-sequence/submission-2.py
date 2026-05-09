class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        mySet = set(nums)
        count = 0

        for num in mySet:
            if num - 1 not in mySet: #we know we are at start of seq
                length = 1
                while num + length in mySet:
                    length += 1
                count = max(count, length)
        
        return count
