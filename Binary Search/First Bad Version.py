def isBadVersion(version: int) -> bool:
    return version %2 == 0

class Solution:
    def firstBadVersion(self, number: int) -> int:
        left_index, right_index = 0, number
        while left_index < right_index:
            middle_index = (left_index + right_index) // 2
            version_check = isBadVersion(middle_index)

            if version_check:
                right_index = middle_index
            else:
                left_index = middle_index +1

        return left_index

