### Algorithm 1: Brute Force
# time Complexity - O(N^2 * K)

class Solution:
    
    ## Algorithm 1
    def palindromePairs_1(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        result = []
        for i, w1 in enumerate(words):
            for j, w2 in enumerate(words):
                if i == j:
                    continue
                if self.isPalindrome(w1+w2):
                    result.append([i, j])
        
        return result
        
    # Check if input string is palindrome
    def isPalindrome(self, word):
        for i in range(len(word)//2):
            if word[i] != word[-1-i]:
                return False
        return True
