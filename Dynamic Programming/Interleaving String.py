class Solution:
    def isInterleave(self, string_x: str, string_y: str, string_z: str) -> bool:
        if len(string_x) + len(string_y) != len(string_z):
            return False
        
        dp_memoization = {}

        def recursive_search(index_x: int, index_y:int, index_z: int) -> bool:
            if index_z == len(string_z):
                return True
            
            if (index_x, index_y, index_z) in dp_memoization:
                return dp_memoization[(index_x, index_y, index_z)]
            
            check_x, check_y = False, False
            
            if index_x < len(string_x) and string_x[index_x] == string_z[index_z]:
                check_x = recursive_search(index_x +1, index_y, index_z +1)
            if index_y < len(string_y) and string_y[index_y] == string_z[index_z]:
                check_y = recursive_search(index_x, index_y +1, index_z +1)

            dp_memoization[(index_x, index_y, index_z)] = check_x or check_y
            return dp_memoization[(index_x, index_y, index_z)]
        
        return recursive_search(0, 0, 0)

