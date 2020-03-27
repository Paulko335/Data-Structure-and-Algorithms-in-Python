# R-7.22
# Implement a clear( ) method for the FavoritesList class that returns the list
# to empty.

from favorites_list_7_22 import FavoritesList


class FavoritesListWithClear(FavoritesList):

    def clear(self):
        """Clears the list"""
        # connects the header to the trailer and back and reset the size to zero
        self._data._header._next = self._data._trailer
        self._data._trailer._prev = self._data._header
        self._data._size = 0


fav = FavoritesListWithClear()

elements = ["0", "1", "2", "3"]

# first half of the sequence
for element in elements:
    fav.access(element)

print("fav is a FavoriteList class instance")
print("fav contains: ", end="")
print(fav)
print("fav has a length of {}".format(len(fav)))
print("")

print("Clearing fav with clear()")
fav.clear()
print("")

print("fav contains: ", end="")
print(fav)
print("fav has a length of {}".format(len(fav)))
