class Solution:
    def longestCommonSubsequence(self, text_x: str, text_y: str) -> int:
        text_grid = [[0] * (len(text_y) + 1) for _ in range(len(text_x) + 1)]

        for index_x in range(1, len(text_x) +1):
            for index_y in range(1, len(text_y) +1):

                if text_x[index_x -1] == text_y[index_y -1]:
                    text_grid[index_x][index_y] = 1 + text_grid[index_x -1][index_y -1]
                else:
                    text_grid[index_x][index_y] = max(text_grid[index_x -1][index_y], text_grid[index_x][index_y -1])

        return text_grid[len(text_x)][len(text_y)]
    