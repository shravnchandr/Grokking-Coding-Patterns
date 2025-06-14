class Solution:
    def romanToInt(self, roman_number: str) -> int:
        symbol_value = {'I':1, 'V': 5, 'X': 10, 
        'L': 50, 'C': 100, 'D': 500, 'M': 1000, }

        int_number, index = 0, 0
        while index < len(roman_number):
            symbol = roman_number[index]

            if index < len(roman_number) -1 and symbol_value[roman_number[index]] < symbol_value[roman_number[index +1]]:
                int_number = int_number + symbol_value[roman_number[index +1]] - symbol_value[symbol]
                index = index + 2
            
            else:
                int_number = int_number + symbol_value[symbol]
                index = index + 1

        return int_number
