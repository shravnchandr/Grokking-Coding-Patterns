from typing import List


class Solution:
    def totalFruit(self, fruits_list: List[int]) -> int:
        last_seen, fruit_types = dict(), list()
        left_index, right_index = 0, 0
        max_fruits = 0

        while right_index < len(fruits_list):
            fruit = fruits_list[right_index]
            
            last_seen[fruit] = right_index

            if len(fruit_types) < 2 and fruit not in fruit_types:
                fruit_types.append(fruit)

            if fruit not in fruit_types:
                max_fruits = max(right_index - left_index, max_fruits)
                
                fruit_x, fruit_y = fruit_types
                if last_seen[fruit_x] < last_seen[fruit_y]:
                    left_index = last_seen[fruit_x] +1
                    fruit_types.remove(fruit_x)
                else:
                    left_index = last_seen[fruit_y] +1
                    fruit_types.remove(fruit_y)

                fruit_types.append(fruit)

            right_index = right_index +1

        max_fruits = max(right_index - left_index, max_fruits)
        return max_fruits
    

