class Solution:
    def isHappy(self, number: int) -> bool:
        
        number_list = [int(char) for char in str(number)]
        for _ in range(25):
            new_number = 0

            for num in number_list:
                new_number = new_number + num ** 2

            if new_number == 1:
                return True
            
            number_list = [int(char) for char in str(new_number)]

        return False
