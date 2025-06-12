class Solution:
    def isPalindrome(self, number: int) -> bool:
        if number < 0:
            return False
        
        return str(number) == str(number)[::-1]
        