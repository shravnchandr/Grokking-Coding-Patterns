from collections import Counter


class Solution:
    def isAnagram(self, string_x: str, string_y: str) -> bool:        
        if len(string_x) != len(string_y):
            return False
            
        char_count_x = Counter(string_x)
        char_count_y = Counter(string_y)
            
        for char, count in char_count_x.items():
            if char not in char_count_y or char_count_y[char] != count:
                return False
                
        return True