class Solution(object):
    def countVowelSubstrings(self, word):
        """
        :type word: str
        :rtype: int
        """
        vowels = {'a','e','i','o','u'}

        counter = 0

        for i in range(len(word)):
            for j in range(i,len(word)+1):
                sub = set(word[i:j])
                if sub.issubset(vowels) and vowels.issubset(sub):
                    counter+=1

        return counter