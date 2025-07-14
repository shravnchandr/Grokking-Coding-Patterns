class Solution:
    def myPow(self, number: float, exponent: int) -> float:                
        if exponent < 0:
            number, exponent = 1 / number, -exponent

        result = 1
        while exponent > 0:
            if exponent % 2 == 1:
                result = result * number
            
            number = number * number
            exponent = exponent // 2

        return result
    