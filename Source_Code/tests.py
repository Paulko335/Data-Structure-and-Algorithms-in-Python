ma_liste = [0, 1, 2, 3]
print(ma_liste)

ma_liste2 = [i for i in range(10) if i < 7]
print(ma_liste2)

mon_generateur = (i for i in range(10) if i < 7)
print(next(mon_generateur))
print(next(mon_generateur))
print(next(mon_generateur), "\n")


def generateur(début, fin, pas):
    while début < fin:
        yield début
        début += pas

mon_gen = generateur(0, 20, 2)
print(next(mon_gen))
print(next(mon_gen))
print(next(mon_gen))

