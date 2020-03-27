# R-7.20
# Implement a reset counts( ) method for the FavoritesList class that resets
# all elements’ access counts to zero (while leaving the order of the list

from favorites_list_7_23 import FavoritesList


class FavoritesListWithReset(FavoritesList):

    def reset_counts(self):
        """reset count to zero for every item of the list"""
        for item in self._data:
            item._count = 0


fav = FavoritesListWithReset()

elements = ["0", "1", "2", "3"]

# first half of the sequence
for element in elements:
    fav.access(element)

print("fav is a FavoriteList class instance")
print("fav contains: ", end="")
print(fav)
print("")

print("Resetting counts")
fav.reset_counts()
print("")

print("fav contains: ", end="")
print(fav)
