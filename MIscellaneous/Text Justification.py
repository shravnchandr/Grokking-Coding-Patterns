from typing import List


class Solution:
    def fullJustify(self, words_list: List[str], max_width: int) -> List[str]:

        final_list = []
        index = 0

        while index < len(words_list):
            current_list, current_count = [], 0

            while index < len(words_list) and current_count + len(words_list[index]) <= max_width:
                current_list.append(words_list[index])
                current_list.append(' ')

                current_count = current_count + len(words_list[index]) +1
                index = index +1

            if current_count -1 == max_width:
                current_list.pop()

            elif index == len(words_list) or len(current_list) == 2:
                while current_count != max_width:
                    current_list[-1] = current_list[-1] + ' '
                    current_count = current_count +1

            else:
                current_list.pop()
                current_count = current_count -1

                while current_count != max_width:
                    current_index = 1

                    while current_index < len(current_list) and current_count != max_width:
                        current_list[current_index] = current_list[current_index] + ' '

                        current_count = current_count +1
                        current_index = current_index +2

            final_list.append(''.join(current_list))
                
        return final_list                        
