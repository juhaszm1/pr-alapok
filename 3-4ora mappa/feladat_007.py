# feladat_007

"""
Kerjunk be egy jegyet 1-5 es irassunk ki egy megadott jegyú
erteket szammal es szoveggel
"""

jegy = int(input("kerek egy egyet 1-5"))
if jegy == 5:
    print(f"A jegyed {jegy} jeles. ")
elif jegy == 4:
    print(f"A jegyed {jegy} jo. ")
elif jegy == 3:
    print(f"A jegyed {jegy} kozepes. ")
elif jegy == 2:
    print(f"A jegyed {jegy} elegseges. ")
elif jegy == 1:
    print(f"A jegyed {jegy} elegtelen. ")
else:
    print(f"A jegyed {jegy} ami nem megfelelo ")