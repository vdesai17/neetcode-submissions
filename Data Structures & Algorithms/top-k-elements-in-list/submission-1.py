import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        frequency = {}
        for i in range(0, len(nums)):
            frequency[nums[i]] = frequency.get(nums[i],0) + 1
        
        return heapq.nlargest(k, frequency.keys(), frequency.get)

