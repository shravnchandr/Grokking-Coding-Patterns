from typing import List


class Solution:
    def jump(self, numbers_list: List[int]) -> int:
        list_length = len(numbers_list)
        
        jump_count = [0] * list_length
        for index in range(len(numbers_list) -2, -1, -1):
            index_jump = numbers_list[index]
            
            if index_jump == 0:
                jump_count[index] = float('inf')

            elif index + index_jump >= list_length -1:
                jump_count[index] = 1

            else:
                jump_count[index] = min(jump_count[index +1: index + index_jump +1], default=0) +1

        return jump_count[0]
    

    def jump(self, numbers_list: List[int]) -> int:
        list_length = len(numbers_list)
        
        jump_count = 0
        current_end, farthest = 0, 0

        for index in range(list_length -1):
            farthest = max(farthest, index + numbers_list[index])

            if index == current_end:
                jump_count = jump_count +1
                current_end = farthest

                if current_end >= list_length -1:
                    return jump_count
                
        return jump_count

    
