#https://leetcode.com/problems/rectangle-area/
from collections import namedtuple
Point = namedtuple('Point',['x','y'])

class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        def rectSize(rect):
            return (rect[1].x - rect[0].x) * (rect[1].y - rect[0].y)

        def isIntersect(rect1,rect2):
            return ( (rect2[1].x >= rect1[0].x >= rect2[0].x or rect1[1].x >= rect2[0].x >= rect1[0].x) and
                     (rect2[1].y >= rect1[0].y >= rect2[0].y or rect1[1].y >= rect2[0].y >= rect1[0].y)
                    )

        def intersectLength(x1,x2,x3,x4):
            arr = [x1,x2,x3,x4]
            arr.sort()
            return arr[2] - arr[1]

        rect1 = (Point(A,B),Point(C,D))
        rect2 = (Point(E,F),Point(G,H))

        if isIntersect(rect1,rect2):
            intersectSize = intersectLength(A,C,E,G) * intersectLength(B,D,F,H)
        else:
            intersectSize = 0

        return rectSize(rect1) + rectSize(rect2) - intersectSize