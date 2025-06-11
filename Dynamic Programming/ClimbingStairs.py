class Solution:
    def climbStairs(self, number: int) -> int:
        if number < 2:
            return number

        dp_storage = [0] * (number +1)
        dp_storage[0], dp_storage[1] = 1, 1

        for index in range(2, number +1):
            dp_storage[index] = dp_storage[index -2] + dp_storage[index -1]

        return dp_storage[number]