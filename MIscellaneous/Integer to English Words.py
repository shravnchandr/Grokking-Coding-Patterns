class Solution:
    def numberToWords(self, number: int) -> str:
        if number == 0:
            return 'Zero'

        number_list = []
        while number > 0:
            number_list.append(number % 1000)
            number = number // 1000

        number_list = number_list[::-1]
        words = ['Billion', 'Million', 'Thousand', '']

        ten_multiples = {
            10:'Ten', 20:'Twenty', 30:'Thirty', 
            40:'Forty', 50:'Fifty', 60:'Sixty', 
            70:'Seventy', 80:'Eighty', 90:'Ninety',
        }

        one_nineteen = {
            1:'One', 2:'Two', 3:'Three', 
            4:'Four', 5:'Five', 6:'Six',
            7:'Seven', 8:'Eight', 9:'Nine',
            10:'Ten',
            11:'Eleven', 12:'Twelve', 13:'Thirteen', 
            14:'Fourteen', 15:'Fifteen', 16:'Sixteen', 
            17:'Seventeen', 18:'Eighteen', 19:'Nineteen',
        }

        final_string = ''
        while number_list:
            current_number = number_list.pop()
            temp_list = []

            if current_number == 0:
                words.pop()
                continue

            hundred_digit = current_number // 100
            remaining_digit = current_number % 100

            if hundred_digit != 0:
                temp_list.append(f'{one_nineteen[hundred_digit]} Hundred')

            if remaining_digit != 0:
                if remaining_digit in one_nineteen:
                    temp_list.append(one_nineteen[remaining_digit])
                else:
                    ten_digit = (remaining_digit // 10) * 10
                    remaining_digit = remaining_digit % 10

                    temp_list.append(ten_multiples[ten_digit])

                    if remaining_digit != 0:
                        temp_list.append(one_nineteen[remaining_digit])

            final_string = ' '.join(temp_list + [words.pop(), final_string])

        return final_string.strip()
    