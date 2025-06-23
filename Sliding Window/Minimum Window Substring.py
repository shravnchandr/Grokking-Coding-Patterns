from collections import Counter, defaultdict


class Solution:
    def minWindow(self, main_string: str, sub_string: str) -> str:
        sub_string_counter = Counter(sub_string)
        main_string_counter = defaultdict(int)

        window_string = main_string + sub_string

        left_index, right_index = 0, 0
        while right_index < len(main_string):
            right_char = main_string[right_index]

            if right_char in sub_string_counter:
                main_string_counter[right_char] = main_string_counter[right_char] +1

                flag = True
                for sub_char, sub_count in sub_string_counter.items():
                    if main_string_counter[sub_char] < sub_count:
                        flag = False
                        break

                if flag:
                    while left_index < right_index:
                        left_char = main_string[left_index]

                        if left_char not in sub_string_counter:
                            left_index = left_index +1

                        else:
                            if main_string_counter[left_char] > sub_string_counter[left_char]:
                                main_string_counter[left_char] = main_string_counter[left_char] -1
                                left_index = left_index +1
                            else:
                                break

                    if (right_index - left_index +1) < len(window_string):
                        window_string = main_string[left_index:right_index +1]

            right_index = right_index +1

        return window_string if window_string != main_string + sub_string else ""
    
