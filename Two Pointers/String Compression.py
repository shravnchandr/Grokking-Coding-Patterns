from typing import List


class Solution:
    def compress(self, string_list: List[str]) -> int:
        if len(string_list) < 2:
            return 1
        
        left_index, right_index = 0, 1
        placeholder_index = 0

        while right_index < len(string_list):

            while right_index < len(string_list) and string_list[left_index] == string_list[right_index]:
                right_index = right_index +1

            string_list[placeholder_index] = string_list[left_index]
            placeholder_index = placeholder_index +1

            character_count = right_index - left_index

            if character_count != 1:
                for number in str(character_count):
                    string_list[placeholder_index] = number
                    placeholder_index = placeholder_index +1
            
            left_index = right_index
            right_index = right_index +1            

        
        return placeholder_index
    