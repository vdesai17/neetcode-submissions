class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        diffSet = {}
        for i in range(0, len(nums)):
            if nums[i] in diffSet:
                return [diffSet.get(nums[i]), i]

            diffSet[target - nums[i]] = i #setting key to be difference of target and integer

