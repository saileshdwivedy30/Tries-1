# Time Complexity : O(m), where m is the length of the inserted/search word
# Space Complexity : O(m * n), m = average word length, n = number of words inserted
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : No

# Your code here along with comments explaining your approach
# I used a nested dictionary (hash map) structure to simulate a Trie.
# Each node represents a character and points to its children.
# Insertion adds characters level by level, marking the end of a word with '$'.
# Search checks if all characters exist and ends at a word marker.
# startsWith verifies prefix presence by traversing without requiring the end marker.

class Trie:

    def __init__(self):
        self.trie = {}

    def insert(self, word: str) -> None:
        node = self.trie
        for char in word:
            if char not in node:
                node[char] = {}
            node = node[char]
        node['$'] = True  # End of word marker

    def search(self, word: str) -> bool:
        node = self.trie
        for char in word:
            if char not in node:
                return False
            node = node[char]
        return '$' in node

    def startsWith(self, prefix: str) -> bool:
        node = self.trie
        for char in prefix:
            if char not in node:
                return False
            node = node[char]
        return True
