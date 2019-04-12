class Solution:
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if word.lower() == word:
            return True
        elif word.upper() == word:
            return True
        elif word[1:] == word[1:].lower():
            return True
        else:
            return False
        
