class Solution(object):
    def defangIPaddr(self, address):
        """
        :type address: str
        :rtype: str
        """
        address = address.replace(".", "[.]")
        return address


class Solution(object):
    def defangIPaddr(self, address):
        """
        :type address: str
        :rtype: str
        """
        arr = address.split(".")
        return "[.]".join(arr)
