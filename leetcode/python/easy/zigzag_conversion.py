# https://leetcode.com/problems/zigzag-conversion/
class Solution:
    # @return a string
    def convert(self, s, nRows):
        if nRows <= 1:
            return s
        i = 0
        nGap = nRows - 2
        colStrings = []
        isGap = False
        # fill col strings
        while i < len(s):
            if isGap:
                colStrings.append(s[i:i + nGap][::-1].rjust(nGap, '\0').center(nRows, '\0'))
                i = i + nGap
            else:
                colStrings.append(s[i:i + nRows].ljust(nRows, '\0'))
                i = i + nRows
            isGap = not isGap
        # rejoin list
        ret = []
        for i in range(nRows):
            for colString in colStrings:
                ret.append(colString[i])

        converted= "".join(ret).replace('\0','')
        if len(converted) != len(s):
            return ''
        else:
            return converted


s = Solution()
print s.convert("ABCDE", 4)
print "end"
