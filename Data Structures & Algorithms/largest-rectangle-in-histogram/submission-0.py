class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        maxArea = 0
        stack = []


        for i in range(len(heights)):
            start = i

            while stack and heights[i] < stack[-1][1]:
                # we reached a wall
                right_wall = i
                left_wall = stack[-1][0]
                area = stack[-1][1] * (right_wall - left_wall)
                # previous height is > curr height we can extend the possible left wall/start for current height
                start = stack[-1][0]
                maxArea = max(area, maxArea)
                stack.pop()
            
            # otherwise
            stack.append((start, heights[i]))
        
        for i in range(len(stack)):

            index, height = stack[i]
            maxArea = max(maxArea, height * (len(heights) - index))
        
        return maxArea

        