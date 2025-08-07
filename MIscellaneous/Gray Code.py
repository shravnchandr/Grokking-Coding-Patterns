from typing import List


class Solution:
    def grayCode(self, number: int) -> List[int]:
        return [index ^ (index >> 1) for index in range(1 << number)]
        