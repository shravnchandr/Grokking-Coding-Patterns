from collections import Counter, defaultdict
from typing import List


class Solution:
    def topKFrequent(self, words_list: List[str], frequency: int) -> List[str]:

        frequency_dict = defaultdict(list)
        for word,freq in Counter(words_list).items():
            frequency_dict[freq].append(word)

        top_frequencies = sorted(frequency_dict.keys(), reverse=True)

        final_list = []
        list_count, index = 0, 0

        while list_count < frequency:
            current_words = sorted(frequency_dict[top_frequencies[index]])
            final_list.extend(current_words[:frequency - list_count])

            list_count, index = list_count + len(current_words), index +1

        return final_list        


    def topKFrequent(self, words_list: List[str], frequency: int) -> List[str]:
        
        word_buckets = [[] for _ in range(len(set(words_list)) +1)]
        for word, freq in Counter(words_list).items():
            word_buckets[freq].append(word)

        final_list = []
        for index in range(len(word_buckets) -1, 0, -1):
            sorted_words = sorted(word_buckets[index])

            if sorted_words:
                for word in sorted_words:
                    if len(final_list) != frequency:
                        final_list.append(word)
                    else:
                        return final_list

        return final_list
