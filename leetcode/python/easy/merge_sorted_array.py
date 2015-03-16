#mergeSortedArray
#https://leetcode.com/problems/merge-sorted-array/
class Solution:
    def merge(self, A, m, B, n):
        A[m:]=[]
        idx=0
        length=len(A)+len(B)
        for i in range(n):
            for j in range(idx,length):
                if j>=len(A):
                    A.extend(B[i:])
                    return
                elif B[i] < A[j]:
                    A.insert(j,B[i])
                    idx=j+1
                    break

s=Solution()
A=[]
s.merge(A,2,[1],1)
print A