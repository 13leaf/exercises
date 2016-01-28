#https://leetcode.com/problems/reverse-bits/
class Solution(object):
    powerCache = [2**x for x in range(32)]

    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        def convertRadixFrom10To2(x):
            bits = []
            while x>0:
                bits.append(str(x % 2))
                x = x/2
            return (''.join(reversed(bits))).rjust(32,'0')

        def convertRadixFrom2To10(bits):
            x = 0
            for i,bit in enumerate(reversed(bits)):
                x += int(bit) * self.powerCache[i]
            return x

        return convertRadixFrom2To10(convertRadixFrom10To2(n)[::-1])