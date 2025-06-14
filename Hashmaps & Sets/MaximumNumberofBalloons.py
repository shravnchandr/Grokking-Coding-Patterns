from collections import Counter


class Solution:
    def maxNumberOfBalloons(self, given_text: str) -> int:
        char_count = Counter(given_text)
        count_list = list()
        
        for char in ('b', 'a', 'l', 'o', 'n'):
            if char in ('l', 'o'):
                count_list.append(char_count.get(char, 0) // 2)
            else:
                count_list.append(char_count.get(char, 0))

        return min(count_list)
    