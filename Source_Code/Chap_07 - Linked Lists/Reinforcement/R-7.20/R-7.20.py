# R-7.20
# Let L be a list of n items maintained according to the move-to-front heuristic.
# Describe a series of O(n) accesses that will reverse L.


from favorites_list_mtf_7_20 import FavoritesListMTF


fav = FavoritesListMTF()

elements = ["0", "1", "2", "3"]

# first half of the sequence
for element in elements:
    fav.access(element)

print("fav is a FavoriteList (Move To Front) class instance")
print("fav contains: ", end="")
print(fav, "\n")

# values inside the list
values = fav.top(len(fav))

for value in values:
    position = fav._find_position(value)    # find the position of the value
    fav._move_up(position)                  # move to first

print("fav contains: ", end="")
print(fav, "\n")
