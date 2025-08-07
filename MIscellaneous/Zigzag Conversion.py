class Solution:
    def convert(self, string: str, row_count: int) -> str:
        if row_count == 1 or row_count >= len(string):
            return string
        
        convert_dict = {index:[] for index in range(row_count)}

        string_index, row_index = 0, 0
        while string_index < len(string):

            if row_index < row_count:
                convert_dict[row_index].append(string[string_index])
                string_index, row_index = string_index +1, row_index +1

            else:
                row_index = row_index -2

                while string_index < len(string) and row_index >= 0:
                    convert_dict[row_index].append(string[string_index])
                    string_index, row_index = string_index +1, row_index -1

                row_index = row_index +2

        final_string = ''
        for index in range(row_count):
            final_string = final_string + ''.join(convert_dict[index])

        return final_string

