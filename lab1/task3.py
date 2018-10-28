"""
Kratak opis programa/potprograma i medjusobnu povezanost:
    - Protrebno je izracunati baricentricne koordinate tocke T s obzirom na trokut zadan s tri vrha
Promjene nacinjene s obzirom na upute:
    - Parametri se primaju kao argumenti
Koristene strukture podataka:
    - Za strukturu podataka se koristila matrix struktura koja je dostupna u numpy biblioteci
Upute za koristenje programa:
    - Program se pokrece pozivom naredbe `python lab1/task3.py` s odgovarajucim argumentima, primjer: `python lab1/task3.py 1 6 11 1 11 1 0 2 0 6 6 1`
Komentar rezultata (brzina, moguce promjene, problemi, nedostaci):
    - Posto je zadatak ogranicen s tri dimenzije ovaj problem je vrlo jednostavno rijesiti koristenjem solve metode dostupne u linalg skupu naredbi u numpy biblioteci
"""

import sys
import numpy as np

# filename + 12 values
if not len(sys.argv) == 13:
    raise BaseException('Nedovoljan broj argumenata')

coeficients = np.matrix([[int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])], [int(sys.argv[4]), int(sys.argv[5]), int(sys.argv[6])], [int(sys.argv[7]), int(sys.argv[8]), int(sys.argv[9])]])
values = np.matrix([[int(sys.argv[10])], [int(sys.argv[11])], [int(sys.argv[12])]])

print np.linalg.solve(coeficients, values)
