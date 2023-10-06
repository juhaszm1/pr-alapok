# feladat_006
# dk9 108-109

"""
ki: gondoltam egy szamra
be: tipp
tipp = gondolt_szam:
elagazas
ha tipp = gondolt_szam:
ki: dicseret
elagazas vege
ki: bucsu
"""

gondoltam_szam = 4
tipp = input('GOndoltam egy szamra. Tippeld meg!')
tipp = int(tipp)
if tipp == gondoltam_szam:
    print("Ugyes")
    print('Gratulalok')
else:
    print('hosszan gondolkodtal rajta?:) ')
    print('Nem erte meg. :) ')
print('Papa')