class Solution(object):
    def subtractProductAndSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        sum = 0
        product = 1
        while n > 0:
            digit = n % 10
            sum += digit
            product *= digit
            n = n // 10

        return product - sum


