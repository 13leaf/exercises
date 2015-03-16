#https://leetcode.com/problems/valid-parentheses/
#Valid Parentheses
class Solution:
    def isValid(self,s):
        brackets={')':'(','}':'{',']':'['}
        openBrackets=[]
        for c in s:
            if c in ['(','{','[']:
                openBrackets.append(c)
            if c in [')','}',']'] :
                if len(openBrackets)==0 or openBrackets[-1] != brackets[c]:
                    return False
                else:
                    openBrackets.pop()
        return len(openBrackets) == 0