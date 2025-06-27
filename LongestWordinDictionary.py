# Time Complexity : O(n * k), where n is number of words and k is average word length
# Space Complexity : O(n * k), for storing all words in a set and building candidates
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : No

# Your code here along with comments explaining your approach
# I used a set to store all words for O(1) lookup.
# For each word, I verified if all prefixes exist in the set.
# If valid, I updated the result based on length and lexicographical order.

class Solution:
    def longestWord(self, words: List[str]) -> str:
        word_set = set(words)
        result = ""

        for word in words:
            valid = True
            for i in range(1, len(word)):
                if word[:i] not in word_set:
                    valid = False
                    break
            if valid:
                if len(word) > len(result) or (len(word) == len(result) and word < result):
                    result = word
        return result
