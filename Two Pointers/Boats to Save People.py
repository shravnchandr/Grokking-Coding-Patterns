from typing import List


class Solution:
    def numRescueBoats(self, people_weights: List[int], weight_limit: int) -> int:
        people_weights = sorted(people_weights)

        boat_count = 0
        left_index, right_index = 0, len(people_weights) -1
            
        while left_index < right_index:
            left_weight, right_weight = people_weights[left_index], people_weights[right_index]

            if left_weight + right_weight <= weight_limit:
                left_index = left_index +1

            boat_count = boat_count +1
            right_index = right_index -1

        return boat_count +1 if left_index == right_index else boat_count

