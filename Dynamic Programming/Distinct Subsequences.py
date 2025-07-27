class Solution:
    def numDistinct(self, big_string: str, small_string: str) -> int:
        
        dp_memoization = {}
        def recursive_search(big_index: int, small_index: int):
            if small_index == len(small_string):
                return 1
            
            if big_index == len(big_string):
                return 0
            
            if (big_index, small_index) in dp_memoization:
                return dp_memoization[(big_index, small_index)]
            
            if big_string[big_index] == small_string[small_index]:
                skip_count = recursive_search(big_index +1, small_index)
                no_skip_count = recursive_search(big_index +1, small_index +1)
                
                final_count = skip_count + no_skip_count
            else:
                final_count = recursive_search(big_index +1, small_index)

            dp_memoization[(big_index, small_index)] = final_count
            return dp_memoization[(big_index, small_index)]
            
        return recursive_search(0, 0)
