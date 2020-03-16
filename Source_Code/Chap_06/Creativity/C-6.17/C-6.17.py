# C-6.17
# In the previous exercise, we assume that the underlying list is initially
# empty. Redo that exercise, this time preallocating an underlying list with
# length equal to the stack’s maximum capacity.


# Modified this in array_stack_6_17.py in Source_Code

# def __init__(self, maxlen=None):
#     """Create an empty stack."""
#     self._data = []
#     self._maxlen = maxlen


# for this

#    def __init__(self, maxlen=None):
#        """Create an empty stack."""
#        if maxlen != None:
#            self._data = [None] * maxlen
#        else:
#            self._data = []
#
#        self._maxlen = maxlen
