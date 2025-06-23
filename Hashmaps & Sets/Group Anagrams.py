from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strings_list: List[str]) -> List[List[str]]:
        anagram_dict = defaultdict(list)

        for string in strings_list:
            count_list = [0] * 26

            for char in string:
                char_index = ord('a') - ord(char)
                count_list[char_index] = count_list[char_index] +1

            anagram_dict[tuple(count_list)].append(string)

        return anagram_dict.values()

        