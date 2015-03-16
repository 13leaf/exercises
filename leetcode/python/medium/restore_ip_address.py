# https://oj.leetcode.com/problems/restore-ip-addresses/
# Restore IP Address
class Solution:
    def _restoreIpAddresses(self, s , addrList):
        if len(s)>(4-len(addrList))*3 or len(s) < (4-len(addrList)):
            return []
        if len(addrList) == 4 and len(s) == 0:
            return ['.'.join(addrList)]
        ret=[]
        for possible in range(1,4):
            if int(s[:possible]) > 255:
                continue
            if s[0] == '0' and possible>1:
                    continue
            ret.extend(self._restoreIpAddresses(s[possible:],addrList+[s[:possible]]))
        return ret
    # @param s, a string
    # @return a list of strings
    def restoreIpAddresses(self, s):
        return list(set(self._restoreIpAddresses(s,[])))
s=Solution()
print s.restoreIpAddresses('010010')