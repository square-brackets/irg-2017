"""
Kratak opis programa/potprograma i medjusobnu povezanost:
    - Potrebno je bilo izracunati i ispisati odredjene izraze, tocnije vrijednost rezultata raznih operacija nad vektorima i matricama
Promjene nacinjene s obzirom na upute:
    - Nisu ucinjene nikakve promjene s obzirom na upute
Koristene strukture podataka:
    - Za strukture podataka su se koristili array i matrix struktura koja je dostupna u numpy biblioteci
Upute za koristenje programa:
    - Program se pokrece pozivom naredbe `python lab1/task1.py`
Komentar rezultata (brzina, moguce promjene, problemi, nedostaci):
    - Posto su se vrsile dosta jednostavne operacije nad vektorima i matricama malih velicina nije nastalo nikakvih problema, te je brzina izvodjenja prihvatljiva
"""

import numpy as np

v1 = np.array([2, 3, -4]) + np.array([-1, 4, -1])
print 'v1:', v1

s = v1 * np.array([-1, 4, -1])
print 's:', s

v2 = np.cross(v1, np.array([2, 2, 4]))
print 'v2:', v2

v3 = np.linalg.norm(v2)
print 'v3:', v3

v4 = -v2
print 'v4:', v4

helpMatrix1 = np.matrix([[1, 2, 3], [2, 1, 3], [4, 5, 1]])
helpMatrix2 = np.matrix([[-1, 2, -3], [5, -2, 7], [-4, -1, 3]])

M1 = helpMatrix1 + helpMatrix2
print 'M1:'
print M1

M2 = helpMatrix1 * helpMatrix2.transpose()
print 'M2:'
print M2

helpMatrix2.transpose()

M2 = helpMatrix1 * helpMatrix2.transpose()
print 'M2:'
print M2

M3 = helpMatrix1 * np.linalg.inv(helpMatrix2)
print 'M3:'
print M3
