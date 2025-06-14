from collections import Counter


class Solution:
    def canConstruct(self, ransom_note: str, magazine_letters: str) -> bool:
        magazine_char_count = Counter(magazine_letters)
        ransom_char_count = Counter(ransom_note)

        for key,value in ransom_char_count.items():
            if key not in magazine_char_count or magazine_char_count[key] < value:
                return False
            
        return True