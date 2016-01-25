#https://leetcode.com/problems/implement-queue-using-stacks/
from collections import deque
class Queue(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self._stack = deque()
        self._first = None

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        if len(self._stack) == 0:
            self._first = x
        self._stack.append(x)

    def pop(self):
        """
        :rtype: nothing
        """
        t = deque()
        while len(self._stack)>0:
            t.append(self._stack.pop())
        ret = t.pop()
        if len(t) > 0:
            self._first = t[-1]
        else:
            self._first = None
        while len(t)>0:
            self._stack.append(t.pop())
        return ret


    def peek(self):
        """
        :rtype: int
        """
        return self._first

    def empty(self):
        """
        :rtype: bool
        """
        return len(self._stack) == 0
