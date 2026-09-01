"""
n cars at given miles away from the starting mile 0 traveling to reach the mile target

given two + int arrays position and speed of same length

position i is the starting mile of the ith car and speed is the speed of the ith car in mph

a car cannot pass another car but it can catch up and travel next to it at the speed of the slower car between the two


if a car catches up to a car fleet at the mile target they will be considered part of the car fleet

return the number of car fleets that arrive at the destination


target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3]

so basically you want to start going through starting from greatest position

do a zip then sort it and then do reverse order so itll be like this
pairs = [(10,2),(8,4),(5,1),(3,3),(0,1)]

then you want to get the value it reaches the target by doing (target - position) / speed
you want to see if the current position and speed is lower than the top of stack
if it is then you dont add it to the stack since it'll be one fleet and end up matching the current speed of the top of stack if it is slower than you add that pair to the top of stack
and you keep doing that and return the len of the stack

"""
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        points = list(zip(position,speed))
        points.sort(reverse=True)
        stack = []

        for p,s in points:
            value = (target - p) / s
            if not stack or value > stack[-1]:
                    stack.append(value)


        return len(stack)
        