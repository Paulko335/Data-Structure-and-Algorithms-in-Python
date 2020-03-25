# R-7.10
# There seems to be some redundancy in the repertoire of the positional
# list ADT, as the operation L.add first(e) could be enacted by the alternative
# L.add before(L.first( ), e). Likewise, L.add last(e) might be performed
# as L.add after(L.last( ), e). Explain why the methods add first
# and add last are necessary.


"""
If we use :L.add_before(L.first( ), e) on an empty list

L.first() returns None, see its definition:
    def first(self):
        "Return the first Position in the list (or None if list is empty)."
    return self._make_position(self._header._next)

If we send p as None to add_before(), _validate is called on p:
  def add_before(self, p, e):
    "Insert element e into list before Position p and return new Position."
    original = self._validate(p)
    return self._insert_between(e, original._prev, original)

If we send p as None to _validate method, it raises a TypeError:
    def _validate(self, p):
        "Return position's node, or raise appropriate error if invalid.
        if not isinstance(p, self.Position):
          raise TypeError('p must be proper Position type')
        if p._container is not self:
          raise ValueError('p does not belong to this container')
        if p._node._next is None:                  # convention for deprecated nodes
          raise ValueError('p is no longer valid')
        return p._node

p is not a proper Position type!

The same problem happens with L.add after(L.last( ), e)
"""
