#   feladat_022
#   Egymasba adott ciklusok

szam = int(input(f"Kerek egy paros szamot: "))
szam_fele = int(szam/2)

darab_karakter = 1
sor = 1
while sor <= 7:
    oszlop = 1
    while oszlop <= darab_karakter:
        print('O ', end='' )
        oszlop = oszlop + 1
    print('')
    darab_karakter = darab_karakter + 1
    sor = sor + 1

darab_karakter = 7
sor = 1
while sor <= 7:
    oszlop = 1
    while oszlop <= darab_karakter:
        print('O ', end='' )
        oszlop = oszlop + 1
    print('')
    darab_karakter = darab_karakter - 1
    sor = sor + 1