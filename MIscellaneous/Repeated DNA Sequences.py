from typing import List


class Solution:
    def findRepeatedDnaSequences(self, dna_string: str) -> List[str]:
        if len(dna_string) < 10:
            return []
        
        seen_sequences = set()
        repeated_sequences = set()
        
        current_sequence = dna_string[:10]
        seen_sequences.add(current_sequence)

        index = 10
        while index < len(dna_string):
            current_sequence = current_sequence[1:] + dna_string[index]

            if current_sequence in seen_sequences:
                repeated_sequences.add(current_sequence)
            else:
                seen_sequences.add(current_sequence)
            
            index = index +1

        return list(repeated_sequences)
        
        