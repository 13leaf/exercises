#https://leetcode.com/problems/count-primes/
class Solution(object):

    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        primes = [True for x in range(n)]
        for i in range(2,int(n ** 0.5) + 1):
            if not primes[i]:
                continue
            for j in range(i*i,n,i):
                primes[j] = False
        return max(primes.count(True) - 2,0)