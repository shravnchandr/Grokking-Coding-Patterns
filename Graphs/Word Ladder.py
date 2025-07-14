from collections import defaultdict, deque
from typing import List


class Solution:
    def ladderLength(self, begin_word: str, end_word: str, word_list: List[str]) -> int:
        if end_word not in word_list:
            return 0
        
        word_mapping = defaultdict(list)
        for word in word_list:
            for index in range(len(word)):
                parent_word = word[:index] + '*' + word[index +1:]
                word_mapping[parent_word].append(word)

        word_queue = deque()
        word_queue.append((begin_word, 1))

        seen_words = set()
        min_length = float('inf')

        while word_queue:
            current_word, current_level = word_queue.popleft()

            if current_word in seen_words:
                continue

            if current_word == end_word:
                min_length = min(min_length, current_level)
                continue

            seen_words.add(current_word)

            next_words = list()
            for index in range(len(current_word)):
                parent_word = current_word[:index] + '*' + current_word[index +1:]
                next_words.extend(word_mapping[parent_word])

            for word in next_words:
                if word not in seen_words:
                    word_queue.append((word, current_level +1))

        return min_length if min_length != float('inf') else 0
