# https://leetcode.com/problems/roman-to-integer/
class Solution:
    def romanToInt(self,s):
        s=s.strip().upper()
        symbolMap={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        lastSymbolVal=symbolMap[s[0]]
        r=0
        trans=0
        for i in range(len(s)) :
            p=symbolMap[s[i]]
            if lastSymbolVal > p:
                lastSymbolVal = p
                r += trans
                trans = p
            elif lastSymbolVal < p:
                lastSymbolVal = p
                r+= p - trans
                trans = 0
            else:
                trans+=p
        r=r+trans
        return r
s=Solution()
print s.romanToInt("MCMXCVI")
print s.romanToInt("MMMCCCXXXIII")
print s.romanToInt('XXV')