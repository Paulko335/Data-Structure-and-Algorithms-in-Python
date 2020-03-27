# R-7.18
# Given the set of element {a,b,c,d,e, f } stored in a list, show the final state
# of the list, assuming we use the move-to-front heuristic and access the elements
# according to the following sequence: (a,b,c,d,e, f ,a,c, f ,b,d,e).


from favorites_list_mtf_7_18 import FavoritesListMTF


fav = FavoritesListMTF()

elements = ["a", "b", "c", "d", "e", "f"]

# first half of the sequence
for element in elements:
    fav.access(element)

# second half of the sequence
second_half = ["a", "c", "f", "b", "d", "e"]
for element in second_half:
    fav.access(element)

print("fav is a FavoriteList (Move To Front) class instance")
print("fav contains: ", end="")
print(fav, "\n")
