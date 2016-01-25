#https://leetcode.com/problems/implement-stack-using-queues/
from collections import deque

class Stack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self._queue = deque()

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self._queue.append(x)


    def pop(self):
        """
        :rtype: nothing
        """
        t = deque()
        while len(self._queue) > 1:
            t.append(self._queue.popleft())
        ret = self._queue.popleft()

        while len(t) > 0:
            self._queue.append(t.popleft())
        return ret


    def top(self):
        """
        :rtype: int
        """
        t = deque()
        while len(self._queue) > 1:
            t.append(self._queue.popleft())
        ret = self._queue[0]
        t.append(self._queue.popleft())

        while len(t) > 0:
            self._queue.append(t.popleft())
        return ret


    def empty(self):
        """
        :rtype: bool
        """
        return len(self._queue) == 0
