from collections import defaultdict


class Solution:
    def checkInclusion(self, sub_string: str, main_string: str) -> bool:
        sub_char_count, main_char_count = defaultdict(int), defaultdict(int)
        for char in sub_string:
            sub_char_count[char] = sub_char_count[char] +1

        left_index, right_index = 0, 0
        while right_index < len(main_string):
            right_char = main_string[right_index]

            if right_char in sub_char_count:
                main_char_count[right_char] = main_char_count[right_char] +1

                if sub_char_count[right_char] < main_char_count[right_char]:
                    
                    while main_string[left_index] != right_char:
                        left_char = main_string[left_index]
                        main_char_count[left_char] = main_char_count[left_char] -1
                        left_index = left_index +1

                    main_char_count[left_char] = main_char_count[left_char] -1
                    left_index = left_index +1

                if (right_index - left_index +1) == len(sub_string) and main_char_count == sub_char_count:
                    return True
                
            else:
                main_char_count = defaultdict(int)
                left_index = right_index +1

            right_index = right_index +1

        return False
    