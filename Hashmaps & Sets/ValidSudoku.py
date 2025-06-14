from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        for index in range(9):
            
            board_set = set()
            for row_index in range(9):
                element = board[row_index][index]

                if element != '.': 
                    if element not in board_set:
                        board_set.add(element)
                    else:
                        return False

            board_set = set()      
            for column_index in range(9):
                element = board[index][column_index]

                if element != '.': 
                    if element not in board_set:
                        board_set.add(element)
                    else:
                        return False

        
        for index in range(0,9,3):

            for column_index in range(0,9,3):

                board_set = set()    
                for row_index in range(index, index+3):
                    element_slice = board[row_index][column_index:column_index +3]

                    for element in element_slice:
                        if element != '.': 
                            if element not in board_set:
                                board_set.add(element)
                            else:
                                return False


        return True