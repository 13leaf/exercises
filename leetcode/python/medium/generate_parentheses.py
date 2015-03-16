# Generate Parentheses
# https://oj.leetcode.com/problems/generate-parentheses/
class Solution:
    # @param an integer
    # @return a list of string
    def generateParenthesis(self, n):
        return self._generateParenthesis(n,dict())

    def getFactors(self,n,capture=None):
        if capture is None:
            capture=dict()
        if n < 0:
            return []
        if n == 1:
            return [[1]]
        if n in capture:
            return capture[n]
        ret=[]
        for i in range(1,n):
            ret.append([i,n-i])
            for x in self.getFactors(n-i,capture):
                t1,t2=[i]+x,x+[i]
                if not t1 in ret:
                    ret.append(t1)
                if not t2 in ret:
                    ret.append(t2)
        capture[n]=ret
        return ret

    def _generateParenthesis(self, n,capture):
        if n < 0:
            return []
        if n == 1:
            return ['()']
        if n in capture:
            return capture[n]
        ret=[]
        for possible in range(2,n):
            childParenthesis=self._generateParenthesis(possible,capture)
            for parenthesis in childParenthesis:
                ret.append('('*(n-possible) + parenthesis + ')'*(n-possible))
        for factors in self.getFactors(n):
            res=self._generateParenthesis(factors[0],capture)
            for factor in factors[1:]:
                res=[x+y for x in res for y in self._generateParenthesis(factor,capture)]
            ret.extend(res)
        capture[n]=list(set(ret))
        return capture[n]


s=Solution()
print s._generateParenthesis(8,dict())