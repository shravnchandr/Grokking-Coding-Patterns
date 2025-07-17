from typing import List


class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_of_word = False


class Trie:
    def __init__(self):
        self.root_node = TrieNode()
    
    def insert_word(self, word: str) -> None:
        current_node = self.root_node
        
        for char in word:
            if char not in current_node.children:
                current_node.children[char] = TrieNode()
            current_node = current_node.children[char]

        current_node.end_of_word = True

    def search_word(self, word: str) -> bool:
        current_node = self.root_node
        
        for char in word:
            if char not in current_node.children:
                return False
            current_node = current_node.children[char]

        return current_node.end_of_word

    def starts_with(self, prefix: str) -> bool:
        current_node = self.root_node
        
        for char in prefix:
            if char not in current_node.children:
                return False
            current_node = current_node.children[char]

        return True


class Solution:
    def wordBreak(self, string: str, word_dict: List[str]) -> bool:
        dictionary_trie = Trie()
        for word in word_dict:
            dictionary_trie.insert_word(word)

        dp_memoization = {}

        def recursive_search(index: int) -> bool:
            if index == len(string):
                return True
            
            if index in dp_memoization:
                return dp_memoization[index]
            
            current_node = dictionary_trie.root_node
            
            for jndex in range(index, len(string)):
                char = string[jndex]

                if char not in current_node.children:
                    break
                current_node = current_node.children[char]

                if current_node.end_of_word:
                    can_break = recursive_search(jndex +1)

                    if can_break:
                        dp_memoization[index] = True
                        return dp_memoization[index]
                    
            dp_memoization[index] = False
            return dp_memoization[index]            

        return recursive_search(0)
        