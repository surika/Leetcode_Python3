# My Solution
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] != 9:
                digits[i] += 1
                return digits
            else:
                digits[i] = 0
        digits.insert(0, 1)
        return digits
            
# A Better Solution
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        string = ''
        for digit in digits:
            string += str(digit)
        number = int(string)  + 1
        st_ls = list(str(number))
        digits = [int(c) for c in st_ls]
        return digits