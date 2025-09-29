from collections import defaultdict
from typing import List


class Solution:
    def findLadders(self, begin_word: str, end_word: str, word_list: List[str]) -> List[List[str]]:
        if end_word not in word_list:
            return []
        
        word_list.append(begin_word)

        word_mapping = defaultdict(list)
        generic_mapping = defaultdict(list)
        for word in word_list:
            for index in range(len(word)):
                generic_word = word[:index] + '*' + word[index +1:]

                word_mapping[generic_word].append(word)
                generic_mapping[word].append(generic_word)

        word_list.pop()

        final_list, current_list = [], [begin_word]
        seen_words = set()

        min_level = len(word_list) +1

        def depth_first_search(current_word: str, current_level: int) -> None:
            nonlocal min_level, final_list

            if current_word == end_word:
                if current_level < min_level:
                    final_list = [current_list[::]]
                    min_level = current_level
                elif current_level == min_level:
                    final_list.append(current_list[::])

            if current_level > min_level:
                return

            seen_words.add(current_word)

            next_words = set()
            for generic_word in generic_mapping[current_word]:
                for word in word_mapping[generic_word]:
                    if word not in seen_words:
                        next_words.add(word)

            for word in next_words:
                if word not in seen_words:
                    current_list.append(word)
                    depth_first_search(word, current_level +1)
                    current_list.pop()

            seen_words.remove(current_word)

        depth_first_search(begin_word, 1)
        return final_list
