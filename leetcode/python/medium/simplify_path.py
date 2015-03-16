# Simplify Path
# https://oj.leetcode.com/problems/simplify-path/
class Solution:
    # @param path, a string
    # @return a string
    def simplifyPath(self, path):
        pathList=path.split('/')
        ret=[]
        for p in pathList:
            if p in ['','.']:
                continue
            if p == '..':
                if len(ret)>0:
                    ret.pop()
            else:
                ret.append(p)
        return '/'+'/'.join(ret)
s=Solution()
print s.simplifyPath('/../')