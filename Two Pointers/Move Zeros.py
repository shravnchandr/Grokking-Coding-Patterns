from typing import List


class Solution:
    def moveZeroes(self, numbers_list: List[int]) -> None:

        zero_index = 0
        while zero_index < len(numbers_list) and numbers_list[zero_index] != 0:
            zero_index = zero_index +1
        num_index = zero_index +1
        
        while num_index < len(numbers_list):
            if numbers_list[num_index] != 0:
                numbers_list[zero_index], numbers_list[num_index] = numbers_list[num_index], numbers_list[zero_index]
                
                while numbers_list[zero_index] != 0:
                    zero_index = zero_index +1
                    
            num_index = num_index +1
            
        