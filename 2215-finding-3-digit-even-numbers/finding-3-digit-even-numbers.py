class Solution(object):
    def findEvenNumbers(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        from collections import Counter

        count = Counter(digits)
        result = []

        for num in range(100, 1000):
            if num % 2 == 0:  # Must be even
                c = Counter([int(d) for d in str(num)])
                if all(count[d] >= c[d] for d in c):  # Check if digits are available
                    result.append(num)

        return result
