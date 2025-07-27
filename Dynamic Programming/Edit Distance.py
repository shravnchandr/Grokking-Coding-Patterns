class Solution:
    def minDistance(self, start_word: str, end_word: str) -> int:
        
        dp_memoization = {}
        def recursive_search(start_index: int, end_index: int) -> int:
            if end_index == len(end_word):
                return len(start_word) - start_index
            
            if start_index == len(start_word):
                return len(end_word) - end_index
            
            if (start_index, end_index) in dp_memoization:
                return dp_memoization[(start_index, end_index)]
            
            if start_word[start_index] == end_word[end_index]:
                return recursive_search(start_index +1, end_index +1)
            
            add_cost = recursive_search(start_index, end_index +1) +1
            subtract_cost = recursive_search(start_index +1, end_index) +1
            replace_cost = recursive_search(start_index +1, end_index +1) +1
            
            dp_memoization[(start_index, end_index)] = min(add_cost, subtract_cost, replace_cost)
            return dp_memoization[(start_index, end_index)]
        
        return recursive_search(0, 0)
    