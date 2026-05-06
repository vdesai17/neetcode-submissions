class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        #we know sets contain only distinct values 
        mySet = set()

        for i in range(0 , len(nums)): #loop over intgers in nums
            mySet.add(nums[i]) #add each integer into mySet
        
        #if the size of mySet and nums is different we know duplicate exists we can return true
        if len(nums) != len(mySet):
            return True
        return False