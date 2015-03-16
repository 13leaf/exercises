#remove duplicate from sorted array
#https://leetcode.com/problems/remove-duplicates-from-sorted-array/
class Solution:
    def removeDuplicates(self, A):
        #use place very slow
        # if len(A) == 0: return 0
        # max=A[0]
        # for i in range(1,len(A)):
        #     j=i
        #     while True:
        #         if j == len(A): return i
        #         if A[j] > max:
        #             max = A[j]
        #             A[j] = A[i]
        #             A[i] = max
        #             break
        #         j=j+1
        # return len(A)
        #use sort very quick
        if len(A) == 0: return 0
        max=A[-1]
        for i in range(1,len(A)):
            if A[i-1] == A[i]:
                A[i-1]=max
        A.sort()
        return A.index(max)+1


s=Solution()
list=[x for y in range(-999,3447) for x in [y,y]]
print s.removeDuplicates(list)