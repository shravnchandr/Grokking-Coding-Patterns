from typing import List


class Solution:
    def carFleet(self, target_position: int, position_list: List[int], speed_list: List[int]) -> int:
        position_speed = zip(position_list, speed_list)
        position_speed = sorted(position_speed, key= lambda x: x[0])

        car_fleet = list()
        for position, speed in position_speed[::-1]:
            time_taken = (target_position - position) / speed

            if car_fleet and car_fleet[-1] >= time_taken:
                continue
            else:
                car_fleet.append(time_taken)

        return len(car_fleet)
    
