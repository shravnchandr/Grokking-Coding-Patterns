class Solution:
    def isPerfectSquare(self, number: int) -> bool:
        left_index, right_index = 0, number
        while left_index <= right_index:
            middle_index = (left_index + right_index) // 2
            middle_number = middle_index ** 2

            if middle_number < number:
                left_index = middle_index +1
            elif middle_number > number:
                right_index = middle_index -1
            else:
                return True

        return False

        