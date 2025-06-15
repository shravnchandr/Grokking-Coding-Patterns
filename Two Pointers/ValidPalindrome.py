class Solution:
    def isPalindrome(self, string: str) -> bool:
        
        left_index, right_index = 0, len(string) -1
        while left_index < right_index:
            left_char, right_char = string[left_index].lower(), string[right_index].lower()

            if left_char.isalnum() and right_char.isalnum():
                if left_char != right_char:
                    return False
                else:
                    left_index, right_index = left_index +1, right_index -1
            
            if not left_char.isalnum():
                left_index = left_index +1
            if not right_char.isalnum():
                right_index = right_index -1
                 
        return True