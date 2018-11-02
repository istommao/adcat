

class LinkedNode(object):

    def __init__(self, val, _next=None):
        self._next = _next
        self.val = val

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, node):
        self._next = node
