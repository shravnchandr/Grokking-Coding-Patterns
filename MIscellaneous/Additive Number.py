class Solution:
    def isAdditiveNumber(self, number_string: str) -> bool:

        numbers_list = []
        def recursive_function(string_index: int) -> bool:
            if string_index >= len(number_string):
                return True
            
            if not numbers_list:
                left_number = number_string[string_index]
                left_index = string_index +1

                while len(left_number) != len(number_string):
                    right_number = number_string[left_index]

                    for right_index in range(left_index +1, len(number_string)):
                        current_sum = str(int(left_number) + int(right_number))

                        for index in range(len(current_sum)):
                            if 


            

        