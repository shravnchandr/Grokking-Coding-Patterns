from collections import defaultdict


class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        stone_counter = defaultdict(int)
        for stone in stones:
            stone_counter[stone] = stone_counter[stone] +1
        
        final_count = 0
        for jewel in jewels:
            final_count = final_count + stone_counter[jewel]

        return final_count
    