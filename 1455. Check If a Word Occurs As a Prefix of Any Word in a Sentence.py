class Solution(object):
    def isPrefixOfWord(self, sentence, searchWord):
        """
        :type sentence: str
        :type searchWord: str
        :rtype: int
        """
        array = sentence.split(" ")
        for i in range(len(array)):
            if array[i].startswith(searchWord):
                return i + 1

        return -1


