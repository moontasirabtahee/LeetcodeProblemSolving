
from collections import Counter

class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        s = 0
        count = Counter(stones)
        for i in jewels:
            s += count[i]

        return s