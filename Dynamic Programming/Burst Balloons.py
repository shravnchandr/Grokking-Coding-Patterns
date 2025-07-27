from typing import List


class Solution:
    def maxCoins(self, numbers_list: List[int]) -> int:
        numbers_list = [1] + numbers_list + [1]

        dp_memoization = {}
        def recursive_search(left_index: int, right_index: int) -> int:
            if left_index >= right_index:
                return 0

            if (left_index, right_index) in dp_memoization:
                return dp_memoization[(left_index, right_index)]
            
            max_coins = 0
            for index in range(left_index +1, right_index):
               current_coins = numbers_list[left_index] * numbers_list[index] * numbers_list[right_index]
               other_coins = recursive_search(left_index, index) + recursive_search(index, right_index)

               max_coins = max(current_coins + other_coins, max_coins)

            dp_memoization[(left_index, right_index)] = max_coins
            return dp_memoization[(left_index, right_index)]
        
        return recursive_search(0, len(numbers_list) -1)
    