class Solution:
    def isMatch(self, string: str, pattern: str) -> bool:
        string_length, pattern_length = len(string), len(pattern)

        def recursive_function(string_index: int, pattern_index: int) -> bool:
            if string_index == string_length and pattern_index == pattern_length:
                return True
            
            if (string_index == string_length and pattern_index != pattern_length) or \
                (string_index != string_length and pattern_index == pattern_length):
                return False
            
            string_char, pattern_char = string[string_index], pattern[pattern_index]

            if pattern_char.isalpha():
                if string_char == pattern_char:
                    is_match = recursive_function(string_index +1, pattern_index +1)
                else:
                    is_match = recursive_function(string_index, pattern_index +1)
                
            else:
                if pattern_char == '.':
                    is_match = recursive_function(string_index +1, pattern_index +1)
                else:

                    if pattern[pattern_index -1] == '.':
                        return True 
                    
                    elif pattern[pattern_index -1] != string_char:
                        is_match = recursive_function(string_index, pattern_index +1)

                    else:
                        while string_index < len(string) -1 and string[string_index] == string[string_index +1]:
                            string_index = string_index +1

                        is_match = recursive_function(string_index +1, pattern_index +1)

            return is_match
        
        return recursive_function(0, 0)
    