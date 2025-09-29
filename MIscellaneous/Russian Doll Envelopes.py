from typing import List


class Solution:
    def maxEnvelopes(self, envelopes_list: List[List[int]]) -> int:
        if len(envelopes_list) == 1:
            return 1
        
        envelopes_list = sorted(envelopes_list)

        dp_memoization = {}
        def recursive_function(index: int, current_envelope: List[int]) -> int:
            if index >= len(envelopes_list):
                return 0
            
            if tuple(current_envelope) in dp_memoization:
                return dp_memoization[tuple(current_envelope)]
            
            current_width, current_height = current_envelope
            max_envelopes_count = 0

            while index < len(envelopes_list):
                new_envelope = envelopes_list[index]
                new_width, new_height = new_envelope

                if current_width < new_width and current_height < new_height:
                    current_envelopes_count = recursive_function(index +1, new_envelope) +1
                    max_envelopes_count = max(current_envelopes_count, max_envelopes_count)

                index = index +1

            dp_memoization[tuple(current_envelope)] = max_envelopes_count
            return dp_memoization[tuple(current_envelope)]
        
        max_count = 0
        for index,envelope in enumerate(envelopes_list):
            if tuple(envelope) not in dp_memoization:
                dp_memoization[tuple(envelope)] = recursive_function(index +1, envelope) +1
            
            max_count = max(dp_memoization[tuple(envelope)], max_count)

        return max_count
    