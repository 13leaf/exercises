# https://oj.leetcode.com/problems/letter-combinations-of-a-phone-number/
# Letter Combinations of a phone number
class Solution:
    digitalLetters={'1':'','2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno','7':'pqrs','8':'tuv','9':'wxyz','0':' ','*':''}
    # @return a list of strings, [s1, s2]
    def letterCombinations(self, digits):
        ret=[""]
        for x in digits:
            letters=self.digitalLetters[x]
            ret=[x+y for x in ret for y in letters]
        return ret
s=Solution()
# print {k:list(v) for k,v in s.digitalLetters.items()}
print s.letterCombinations('2')