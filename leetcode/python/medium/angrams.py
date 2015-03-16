# https://oj.leetcode.com/problems/anagrams/
class Solution:
    # @param strs, a list of strings
    # @return a list of strings
    def anagrams(self, strs):
        anagramDict=dict()
        for i in range(len(strs)):
            hashCode=reduce(lambda x,y:x+10**(ord(y)-ord('a')),strs[i],0)
            if not hashCode in anagramDict:
                anagramDict[hashCode]=[]
            anagramDict[hashCode].append(i)
        anagramList=[]
        for k,v in anagramDict.items():
            if len(v)>1:
                for i in v:
                    anagramList.append(strs[i])
        return anagramList
s=Solution()
print s.anagrams(['ad','bc','da','c'])