
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        cars = sorted(zip(position, speed), reverse=True)
        stack = []

        for pos, speed in cars:

            time = (target - pos) / speed
            stack.append(time)
            if len(stack) >= 2 and time <= stack[-2]:
                # if this car the car ahead
                stack.pop()
        
        return len(stack)