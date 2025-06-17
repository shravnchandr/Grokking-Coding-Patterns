from typing import List, Set, Tuple


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        def helperFunction(row_index: int, column_index: int, seen_cells: Set[Tuple[int]], string_index: int) -> bool:
            if row_index < 0 or row_index >= len(board) or column_index < 0 or column_index >= len(board[0]):
                return False
            if (row_index, column_index) in seen_cells:
                return False
            
            if string_index >= len(word):
                return False
            if board[row_index][column_index] != word[string_index]:
                return False

            if string_index == len(word) -1 and board[row_index][column_index] == word[string_index]:
                return True
            
            seen_cells.add((row_index, column_index))
            
            left_check = helperFunction(row_index -1, column_index, seen_cells, string_index +1)
            right_check = helperFunction(row_index +1, column_index, seen_cells, string_index +1)
            up_check = helperFunction(row_index, column_index -1, seen_cells, string_index +1)
            down_check = helperFunction(row_index, column_index +1, seen_cells, string_index +1)

            seen_cells.remove((row_index, column_index))

            return left_check or right_check or up_check or down_check
        
        for row_index in range(len(board)):
            for column_index in range(len(board[0])):
                if board[row_index][column_index] == word[0]:
                    word_check = helperFunction(row_index, column_index, set(), 0)

                    if word_check:
                        return True
                    
        return False

