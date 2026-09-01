from typing import List
import math
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        sort: List[(int, int)] = []
        for i in range(len(position)):
            sort.append((-position[i], speed[i]))

        sort.sort()
        m: int = 0
        groups: int = 0
        for s in sort:
            steps: int = math.floor((target + s[0]) / s[1])
            if steps > m or steps == 0:
                groups += 1
                m = steps

        return groups
                 
    def carFleet_not_working(self, target: int, position: List[int], speed: List[int]) -> int:
        cars: int = 0
        m: int = 0
        m_speed: int = 0

        i: int = 0
        # O(n)
        while i < len(position):
            if position[i] > m:
                m = position[i]
                m_speed = speed[i]
            i += 1

        steps: int = math.floor((target - m) / m_speed)
        for i in range(len(position)):
            car_steps: int = math.floor((target - position[i]) / speed[i])
            if car_steps <= steps:
                cars += 1

        return len(position) - cars + 1

s = Solution()

print(s.carFleet(target=10, position=[8,3,7,4,6,5], speed=[4,4,4,4,4,4]))
print(s.carFleet(target=10, position=[0,4,2], speed=[2,1,3]))
print(s.carFleet(target=10, position=[6,8], speed=[3,2]))
print(s.carFleet(target=12, position=[10,8,0,5,3], speed=[2,4,1,1,3]))
print(s.carFleet(target = 10, position = [4,1,0,7], speed = [2,2,1,1]))
print(s.carFleet(target = 10, position = [1,4], speed = [3,2]))
