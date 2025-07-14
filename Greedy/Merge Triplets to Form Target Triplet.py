from typing import List


class Solution:
    def mergeTriplets(self, triplets_list: List[List[int]], target_triplet: List[int]) -> bool:
        final_triplet = [0, 0, 0]
        for triplet in triplets_list:
            
            values_check = True
            for current_value, target_value in zip(triplet, target_triplet):
                if current_value > target_value:
                    values_check = False

            if values_check:
                final_triplet = [max(current_value, target_value) for current_value, target_value in zip(triplet, final_triplet)]
                
                if final_triplet == target_triplet:
                    return True
            
        return False

