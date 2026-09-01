from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        q = deque() # stores indicies
        ret = []

        for right in range(len(nums)):
            while q and nums[right] > nums[q[-1]]:
                q.pop()
            q.append(right)

            if q[0] <= right - k:
                q.popleft()
            if right >= k - 1:
                ret.append(nums[q[0]])
            
        return ret
        