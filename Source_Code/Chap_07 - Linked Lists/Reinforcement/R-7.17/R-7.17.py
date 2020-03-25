# R-7.17
# In the FavoritesListMTF class, we rely on public methods of the positional
# list ADT to move an element of a list at position p to become the first element
# of the list, while keeping the relative order of the remaining elements
# unchanged. Internally, that combination of operations causes one node to
# be removed and a new node to be inserted. Augment the PositionalList
# class to support a new method, move to front(p), that accomplishes this
# goal more directly, by relinking the existing node.


from favorites_list_mtf_7_17 import FavoritesListMTF


class FavoritesListMTFWIthFrontMethod(FavoritesListMTF):

    def front(self, p):
        """moves p to the first position if it is not already first"""
        if p != self._data.first():
            # to complete the chain, we need to know where those 5 positions are:
            # 1.the header,            2.the old head,
            # 4.the position before p, 5.p,            6.the position after p

            # fixing unknown positions to variables to reroute links them more easily
            old_head = self._data.first()
            prev_p = self._data.before(p)

            if self._data.after(p) is None:     # if p is at the end
                next_p = self._data._trailer    # next_p is the node trailer
            else:
                next_p = self._data.after(p)    # next_p is the position after p

            # connect the header to its next node(p) and back
            self._data._header._next = p._node
            p._node._prev = self._data._header

            # connect p to the second node and back
            p._node._next = old_head._node
            old_head._node._prev = p._node

            # connect the position before the old p to the one after and back
            if next_p is self._data._trailer:
                prev_p._node._next = next_p
                next_p._prev = prev_p
            else:
                prev_p._node._next = next_p._node
                next_p._node._prev = prev_p

    # we override access to use front instead of _move_up
    def access(self, e):
        """Access element e, thereby increasing its access count."""
        p = self._find_position(e)
        if p is None:
            p = self._data.add_last(self._Item(e))
        p.element()._count += 1
        self.front(p)                              # modified self._move_up(p) by self.front(p)


fav = FavoritesListMTFWIthFrontMethod()

print("Testing every access possibilities")
print("fav is a FavoriteList (Move To Front) class instance\n")
# element i has been accessed i times
for i in range(1, 4):
    for j in range(i):
        fav.access(i)
    print("Element {} has been accessed {} times".format(i, i))
    print("fav contains: ", end="")
    print(fav, "\n")

fav.access(2)
fav.access(2)
print("Element 2 has been accessed 2 more times")

print("fav contains: ", end="")
print(fav, "\n")
