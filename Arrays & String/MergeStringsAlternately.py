class Solution:
    def mergeAlternately(self, word_x: str, word_y: str) -> str:
        merged_word = list()

        index_x, index_y = 0, 0
        while index_x < len(word_x) and index_y < len(word_y):
            # merged_word = merged_word + word_x[index_x] + word_y[index_y]
            merged_word.append(word_x[index_x])
            merged_word.append(word_y[index_y])
            index_x, index_y = index_x +1, index_y +1

        while index_x < len(word_x):
            merged_word.append(word_x[index_x])
            index_x = index_x +1

        while index_y < len(word_y):
            merged_word.append(word_y[index_y])
            index_y = index_y +1

        return ''.join(merged_word)
        