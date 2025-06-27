# Time Complexity : O(n * k), where n is number of words in the sentence and k is the average word length
# Space Complexity : O(t), where t is total characters in all roots (Trie size)
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : No

# Your code here along with comments explaining your approach
# I used a Trie to insert all roots.
# Then, for each word in the sentence, I traversed the Trie to find the shortest matching root prefix.
# If found, replaced the word with that root.

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        # Build Trie
        root_node = TrieNode()
        for word in dictionary:
            node = root_node
            for ch in word:
                if ch not in node.children:
                    node.children[ch] = TrieNode()
                node = node.children[ch]
            node.isEnd = True

        def findRoot(word):
            node = root_node
            prefix = ""
            for ch in word:
                if ch not in node.children:
                    return word
                node = node.children[ch]
                prefix += ch
                if node.isEnd:
                    return prefix
            return word

        words = sentence.split()
        replaced = [findRoot(word) for word in words]
        return " ".join(replaced)
