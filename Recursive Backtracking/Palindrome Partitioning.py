from typing import List


class Solution:
    def partition(self, string: str) -> List[List[str]]:
        final_list, current_list = list(), list()

        def recursive_backtracking(index: int):
            if index == len(string):
                current_string = ''.join(current_list)

                if current_string == current_string[::-1]:
                    final_list.append(current_string)
                return
            
            current_list.append(string[index])
            for jndex in range(index +1, len(string)):
                recursive_backtracking(jndex)

            current_string = ''.join(current_list)
            if current_string == current_string[::-1]:
                final_list.append(current_string)

            current_list.pop()

        for index in range(len(string)):
            recursive_backtracking(index)

        return final_list
    