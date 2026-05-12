class Solution:
    def trap(self, height: List[int]) -> int:
        
        max_l = [0] * len(height)
        max_r = [0] * len(height)
        s = 0
        curr_max = 0
        #max_l
        for i in range(0, len(height)):
            curr_max = max(curr_max, height[i])
            max_l[i] = curr_max
        
        #max_r
        curr_max_r = 0
        for i in range(len(height)-1,-1, -1):
            curr_max_r = max(curr_max_r, height[i])
            max_r[i]  = curr_max_r


        for k in range(0, len(height)):
            x = min(max_l[k],max_r[k])
            calc = x - height[k]
            if calc <= 0:
                s += 0
            else:    
                s += calc

        return s    


